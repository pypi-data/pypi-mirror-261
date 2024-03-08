from datetime import datetime
import random
from time import sleep

from neutron.db import api as db_api
from neutron.db import db_base_plugin_common
from neutron.db import _model_query as model_query
from neutron.db import _utils as db_utils
from neutron_lbaas.agent_scheduler import LoadbalancerAgentBinding

from neutron_lbaas_inventory.common import constants
from neutron_lbaas_inventory.common import exceptions as exc
from neutron_lbaas_inventory.db.models import inventory as models

from oslo_db import exception as oslo_db_exc
from oslo_serialization import jsonutils
from oslo_log import log as logging
from oslo_utils import uuidutils
from sqlalchemy.orm import exc as db_exc

LOG = logging.getLogger(__name__)


class InventoryDbPlugin(db_base_plugin_common.DbBasePluginCommon):

    @db_api.retry_if_session_inactive()
    def create_device(self, context, payload):
        device = payload["device"]

        with db_api.context_manager.writer.using(context):
            args = {
                "id": device.get("id") or uuidutils.generate_uuid(),
                "name": device.get("name"),
                "description": device.get("description"),
                "project_id": device["project_id"],
                "shared": device.get("shared", True),
                "admin_state_up": device.get("admin_state_up", True),
                "availability_zone": device.get("availability_zone"),
                "provisioning_status": jsonutils.dumps(
                    {"status": constants.IDLE}),
                "device_info": jsonutils.dumps(device["device_info"]),
            }
            device_db = models.Device(**args)
            context.session.add(device_db)

        return self._device_dict(device_db)

    @db_api.retry_if_session_inactive()
    def delete_device(self, context, id):
        with context.session.begin(subtransactions=True):
            in_use, lb_ids = self._device_in_use(context, id)
            if in_use:
                raise exc.DeviceInUse(device_id=id, loadbalancer_ids=lb_ids)

            in_use, member_ids = self._device_member_in_use(context, id)
            if in_use:
                raise exc.DeviceMemberInUse(device_id=id,
                                            member_ids=member_ids)

            device = self._get_device(context, id)
            context.session.delete(device)

    @db_api.retry_if_session_inactive()
    def get_devices(self, context, filters=None):
        return [
            device
            for device in model_query.get_collection(
                context, models.Device, self._device_dict, filters=filters)
        ]

    @db_api.retry_if_session_inactive()
    def _populate_member_info(self, context, device, device_id):
        members = self.get_members(context,
                                   filters={'device_id': [device_id]})
        device['device_info']['members'] = members
        return device

    @db_api.retry_if_session_inactive()
    def get_device(self, context, id):
        device = self._device_dict(self._get_device(context, id))
        return self._populate_member_info(context, device, id)

    @db_api.retry_if_session_inactive()
    def update_device(self, context, id, payload):
        json_keys = [
            "provisioning_status",
            "device_info",
        ]
        device = payload["device"]
        for key in json_keys:
            if key in device:
                device[key] = jsonutils.dumps(device[key])

        with context.session.begin(subtransactions=True):
            device_db = self._get_device(context, id)
            if device:
                self._check_shared(context, device_db, device)
                device_db.update(device)

        return self._device_dict(device_db)

    @db_api.retry_if_session_inactive()
    def occupy_device(self, context, id, expire=5, request_id=""):
        # The caller may switch to admin context. Parameter request_id
        # is the original request id of the caller.
        if not request_id:
            request_id = context.request_id
        max_wait = 10
        attempt = 0
        occupied = False
        ps = {}
        start_time = datetime.utcnow()
        while not occupied:
            attempt += 1
            try:
                with context.session.begin(subtransactions=True):
                    query = model_query.query_with_hooks(context=context,
                                                         model=models.Device)
                    # Accquire the device row lock
                    device_db = query.filter(
                        models.Device.id == id
                    ).populate_existing().with_for_update().one()
                    device = self._device_dict(device_db)
                    ps = device["provisioning_status"]
                    LOG.debug("Occupy attempt %s Device %s "
                              "provisioning_status is %s",
                              attempt, id, ps)
                    status = ps.get("status", constants.IDLE)
                    ts_str = ps.get("timestamp", "2000-01-01T00:00:00Z")
                    try:
                        ts = datetime.strptime(ts_str[:-1], constants.DT_FMT)
                    except ValueError:
                        ts = datetime(2000, 1, 1, 0, 0)
                    ts_now = datetime.utcnow()
                    ts_delta = (ts_now - ts).total_seconds()

                    if status == constants.BUSY and \
                       0 <= ts_delta < expire:
                        # Device is occupied by another request.
                        # Wait and retry.
                        occupied = False
                    else:
                        # Device is idle or lock expires. Occupy the device.
                        # If provisioning_status data is wrong, which should
                        # be an impossible case, we will also ignore it and
                        # occupy the device.
                        ts_now_str = ts_now.strftime(constants.DT_FMT) + "Z"
                        device_db.provisioning_status = jsonutils.dumps({
                            "status": constants.BUSY,
                            "request_id": request_id,
                            "timestamp": ts_now_str
                        })
                        # Quit the loop and release lock
                        LOG.debug("Complete to occupy device %s "
                                  "after %s attempts. The last "
                                  "provisioning_status %s", id, attempt, ps)
                        occupied = True
                # The device row lock has been released here
            except oslo_db_exc.DBDeadlock as ex:
                # NOTE(qzhao): A request who does not get the row lock
                # may encounter deadlock error. It can retry, and should
                # give up eventually, if it can not acquire the lock.
                LOG.debug("Occupy attempt %s DB deadlock: %s", attempt, ex)
            finally:
                if not occupied:
                    end_time = datetime.utcnow()
                    if (end_time - start_time).total_seconds() < max_wait:
                        # Wait up to 1 second
                        interval = random.uniform(0.5, 1.0)
                        sleep(interval)
                    else:
                        LOG.warning("Fail to occupy device %s "
                                    "after %s attempts. The last "
                                    "provisioning_status %s", id, attempt, ps)
                        another_rid = ps.get("request_id", "unknown")
                        raise exc.DeviceIsBusy(device_id=id,
                                               request_id=another_rid)
        return occupied

    @db_api.retry_if_session_inactive()
    def release_device(self, context, id, request_id=""):
        # The caller may switch to admin context. Parameter request_id
        # is the original request id of the caller.
        if not request_id:
            request_id = context.request_id
        max_wait = 10
        attempt = 0
        released = False
        start_time = datetime.utcnow()
        while not released:
            attempt += 1
            try:
                with context.session.begin(subtransactions=True):
                    query = model_query.query_with_hooks(context=context,
                                                         model=models.Device)
                    # Accquire the device row lock
                    device_db = query.filter(
                        models.Device.id == id
                    ).populate_existing().with_for_update().one()
                    device = self._device_dict(device_db)
                    ps = device["provisioning_status"]
                    LOG.debug("Release attempt %s Device %s "
                              "provisioning_status is %s",
                              attempt, id, ps)
                    status = ps.get("status", constants.IDLE)
                    rid = ps.get("request_id", "unknown")
                    if status == constants.BUSY and rid == request_id:
                        device_db.provisioning_status = jsonutils.dumps({
                            "status": constants.IDLE
                        })
                        LOG.debug("Complete to release device %s", id)
                    else:
                        LOG.warning("Skip to release device %s. "
                                    "Device status is %s and "
                                    "occupier request_id is %s",
                                    id, status, rid)
                    released = True
                # The device row lock has been released here
            except oslo_db_exc.DBDeadlock as ex:
                # NOTE(qzhao): A request who does not get the row lock
                # may encounter deadlock error. It can retry, and should
                # give up eventually, if it can not acquire the lock.
                LOG.debug("Release attempt %s DB deadlock: %s", attempt, ex)
            finally:
                if not released:
                    end_time = datetime.utcnow()
                    if (end_time - start_time).total_seconds() < max_wait:
                        # Wait up to 0.1 second
                        interval = random.uniform(0, 0.1)
                        sleep(interval)
                    else:
                        LOG.warning("Give up releasing device %s "
                                    "after %s attempts.", id, attempt)
                        raise exc.DeviceIsBusy(device_id=id, request_id="")
        return released

    def _get_device(self, context, id):
        try:
            device = model_query.get_by_id(
                context, models.Device, id)
        except db_exc.NoResultFound:
            raise exc.DeviceNotFound(device_id=id)
        return device

    def _device_in_use(self, context, id):
        lb_ids = self.get_bindings(context, filters={'device_id': [id]},
                                   fields=['loadbalancer_id'])
        if len(lb_ids) > 0:
            lbs = ','.join([lb['loadbalancer_id'] for lb in lb_ids])
            return True, lbs
        return False, None

    def _device_member_in_use(self, context, id):
        members = self.get_members(context, filters={'device_id': [id]},
                                   fields=['id'])
        if len(members) > 0:
            member_ids = ''.join([member['id'] for member in members])
            return True, member_ids
        return False, None

    def _device_dict(self, device_db, fields=None):
        json_keys = [
            "provisioning_status",
            "device_info",
        ]

        device = dict((k, device_db[k])
                      for k in device_db.keys() if k not in json_keys)
        for k in json_keys:
            device[k] = self._get_dict(device_db, k)

        return device

    def _get_dict(self, device_db, dict_name, ignore_missing=False):
        json_string = None
        try:
            json_string = getattr(device_db, dict_name)
            json_dict = jsonutils.loads(json_string)
        except Exception:
            if json_string or not ignore_missing:
                msg = "Dictionary %(dict_name)s for device %(id)s is invalid."
                LOG.warning(msg, {"dict_name": dict_name,
                                  "id": device_db.id})
            json_dict = {}
        return json_dict

    def _check_shared(self, context, old_device, new_device):
        new_shared = new_device.get('shared')
        if new_shared is None:
            return
        old_shared = old_device.shared
        device_id = old_device.id
        # Device that no lb exists can change shared from True to False
        if old_shared is True and new_shared is False:
            in_use, lb_ids = self._device_in_use(context, device_id)
            if in_use:
                raise exc.DeviceInUse(device_id=device_id,
                                      loadbalancer_ids=lb_ids)

    @db_api.retry_if_session_inactive()
    def get_bindings(self, context, filters=None, fields=None):
        return [
            binding
            for binding in model_query.get_collection(
                context, LoadbalancerAgentBinding, self._binding_dict,
                filters=filters, fields=fields)
        ]

    def _binding_dict(self, binding_db, fields=None):
        binding = dict((k, binding_db[k])
                       for k in binding_db.keys())
        return db_utils.resource_fields(binding, fields)

    @db_api.retry_if_session_inactive()
    def create_member(self, context, device_id, payload):
        member = payload["member"]

        with db_api.context_manager.writer.using(context):
            args = {
                "id": uuidutils.generate_uuid(),
                "device_id": device_id,
                "type": member["type"],
                "mgmt_ipv4": member.get("mgmt_ipv4"),
                "mgmt_ipv6": member.get("mgmt_ipv6"),
                "device_info": jsonutils.dumps(member["device_info"]),
                "operating_status": jsonutils.dumps(
                    member["operating_status"]),
                "last_error": jsonutils.dumps({})
            }
            member_db = models.DeviceMember(**args)
            context.session.add(member_db)

        return self._member_dict(member_db)

    @db_api.retry_if_session_inactive()
    def delete_member(self, context, id):
        with context.session.begin(subtransactions=True):
            member = self._get_member(context, id)
            context.session.delete(member)

    @db_api.retry_if_session_inactive()
    def get_members(self, context, filters=None, fields=None):
        return [
            member
            for member in model_query.get_collection(
                context, models.DeviceMember, self._member_dict,
                filters=filters, fields=fields)
        ]

    @db_api.retry_if_session_inactive()
    def get_member(self, context, id):
        return self._member_dict(self._get_member(context, id))

    @db_api.retry_if_session_inactive()
    def update_member(self, context, id, payload):
        json_keys = [
            "operating_status",
            "device_info",
            "last_error"
        ]
        member = payload["member"]
        for key in json_keys:
            if key in member:
                member[key] = jsonutils.dumps(member[key])

        with context.session.begin(subtransactions=True):
            member_db = self._get_member(context, id)
            if member:
                member_db.update(member)

        return self._member_dict(member_db)

    def _get_member(self, context, id):
        try:
            member = model_query.get_by_id(
                context, models.DeviceMember, id)
        except db_exc.NoResultFound:
            raise exc.DeviceMemberNotFound(device_member_id=id)
        return member

    def _member_dict(self, member_db, fields=None):
        json_keys = [
            "operating_status",
            "device_info",
            "last_error"
        ]

        member = dict((k, member_db[k])
                      for k in member_db.keys() if k not in json_keys)
        for k in json_keys:
            member[k] = self._get_member_dict(member_db, k)

        return member

    def _get_member_dict(self, member_db, dict_name, ignore_missing=False):
        json_string = None
        try:
            json_string = getattr(member_db, dict_name)
            json_dict = jsonutils.loads(json_string)
        except Exception:
            if json_string or not ignore_missing:
                msg = "Dictionary %(dict_name)s for member %(id)s is invalid."
                LOG.warning(msg, {"dict_name": dict_name,
                                  "id": member_db.id})
            json_dict = {}
        return json_dict

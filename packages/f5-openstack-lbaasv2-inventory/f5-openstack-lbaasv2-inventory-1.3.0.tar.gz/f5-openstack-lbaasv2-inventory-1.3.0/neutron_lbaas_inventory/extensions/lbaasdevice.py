
from neutron.api import extensions as neutron_extensions
from neutron.api.v2 import resource_helper
from neutron_lib.api import converters
from neutron_lib.api import extensions as api_extensions
from neutron_lib.db import constants as db_const
from neutron_lib.plugins import directory

from oslo_log import log as logging
from neutron.api import extensions
from neutron.api.v2 import base as api_base

from neutron_lbaas_inventory.extensions import base
from neutron_lbaas_inventory import extensions as device_extensions
from neutron_lbaas_inventory.common import constants

# Ensure the extension is loaded at startup
neutron_extensions.append_api_extensions_path(device_extensions.__path__)

LOG = logging.getLogger(__name__)

RESOURCE_ATTRIBUTE_MAP = {
    'devices': {
        'id': {'allow_post': False, 'allow_put': False,
               'validate': {'type:uuid': None},
               'is_visible': True,
               'primary_key': True},
        'name': {'allow_post': True, 'allow_put': True,
                 'validate': {'type:string': db_const.NAME_FIELD_SIZE},
                 'default': '',
                 'is_visible': True},
        'description': {'allow_post': True, 'allow_put': True,
                        'validate': {
                            'type:string': db_const.DESCRIPTION_FIELD_SIZE},
                        'is_visible': True, 'default': ''},
        'project_id': {'allow_post': True, 'allow_put': False,
                       'validate': {
                           'type:string': db_const.PROJECT_ID_FIELD_SIZE},
                       'is_visible': True},
        'shared': {'allow_post': True, 'allow_put': True,
                   'default': True,
                   'convert_to': converters.convert_to_boolean,
                   'is_visible': True},
        'admin_state_up': {'allow_post': True, 'allow_put': True,
                           'default': True,
                           'convert_to': converters.convert_to_boolean,
                           'is_visible': True},
        'availability_zone': {'allow_post': True, 'allow_put': True,
                              'is_visible': True},
        'device_info': {'allow_post': True, 'allow_put': True,
                        'is_visible': True},
        'provisioning_status': {'allow_post': False, 'allow_put': True,
                                'is_visible': True},
    },
    'loadbalanceragentbindings': {
        'loadbalancer_id': {'allow_post': False, 'allow_put': False,
                            'validate': {'type:uuid': None},
                            'is_visible': True,
                            'primary_key': True},
        'agent_id': {'allow_post': False, 'allow_put': False,
                     'validate': {'type:uuid': None},
                     'is_visible': True},
        'device_id': {'allow_post': False, 'allow_put': False,
                      'validate': {'type:uuid': None},
                      'is_visible': True},
    },
}

SUB_RESOURCE_ATTRIBUTE_MAP = {
    'members': {
        'parent': {'collection_name': 'devices',
                   'member_name': 'device'},
        'parameters': {
            'id': {'allow_post': False, 'allow_put': False,
                   'validate': {'type:uuid': None},
                   'is_visible': True,
                   'primary_key': True},
            'device_id': {'allow_post': False, 'allow_put': False,
                          'validate': {'type:uuid': None},
                          'is_visible': True},
            'tenant_id': {'allow_post': True, 'allow_put': False,
                          'validate': {'type:not_empty_string':
                                       db_const.PROJECT_ID_FIELD_SIZE},
                          'required_by_policy': True,
                          'is_visible': True},
            'type': {'allow_post': True, 'allow_put': True,
                     'is_visible': True},
            'mgmt_ipv4': {'allow_post': True, 'allow_put': False,
                          'is_visible': True},
            'mgmt_ipv6': {'allow_post': True, 'allow_put': False,
                          'is_visible': True},
            'device_info': {'allow_post': True, 'allow_put': True,
                            'is_visible': True},
            'operating_status': {'allow_post': True, 'allow_put': True,
                                 'is_visible': True},
            'last_error': {'allow_post': False, 'allow_put': True,
                           'is_visible': True}
        }
    }
}


class Lbaasdevice(api_extensions.ExtensionDescriptor):
    """API extension for handling lbaas device."""

    @classmethod
    def get_name(cls):
        return "Lbaas Device"

    @classmethod
    def get_alias(cls):
        return "lbaas-device"

    @classmethod
    def get_description(cls):
        return "Provides a REST API for lbaas device " \
               "operators to manage devices."

    @classmethod
    def get_updated(cls):
        return "2023-03-14T00:00:00-00:00"

    @classmethod
    def get_resources(cls):
        plural_mappings = resource_helper.build_plural_mappings(
            {}, RESOURCE_ATTRIBUTE_MAP)

        # bind service plugin name
        which_plugin = constants.LBAAS_EXTS

        resources = resource_helper.build_resource_info(
            plural_mappings,
            RESOURCE_ATTRIBUTE_MAP,
            which_plugin,
            register_quota=False)

        plugin = directory.get_plugin(which_plugin)

        for collection_name in SUB_RESOURCE_ATTRIBUTE_MAP:
            # Special handling needed for sub-resources with 'y' ending
            # (e.g. proxies -> proxy)
            resource_name = collection_name[:-1]
            parent = SUB_RESOURCE_ATTRIBUTE_MAP[collection_name].get('parent')
            params = SUB_RESOURCE_ATTRIBUTE_MAP[collection_name].get(
                'parameters')
            controller = api_base.create_resource(
                collection_name, resource_name,
                plugin, params,
                allow_bulk=True,
                parent=parent,
                allow_pagination=True,
                allow_sorting=True)
            resource = extensions.ResourceExtension(
                collection_name,
                controller, parent,
                path_prefix=constants.LBAAS_EXTS_PREFIX,
                attr_map=params)
            resources.append(resource)
        return resources

    @classmethod
    def get_plugin_interface(cls):
        return base.LbaasExtensionsPluginBase

    def get_extended_resources(self, version):
        if version == "2.0":
            return RESOURCE_ATTRIBUTE_MAP
        else:
            return {}

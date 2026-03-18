from netbox.plugins import PluginConfig


class NetBoxAccessListsConfig(PluginConfig):
    name = 'netbox_access_lists'
    verbose_name = 'NetBox Access Lists'
    description = 'Manage simple access lists in NetBox'
    version = '0.1.0'
    base_url = 'access-lists'
    min_version = '4.5.0'
    max_version = '4.5.99'


config = NetBoxAccessListsConfig

from extras.plugins import PluginConfig


class NetBoxAccessListsConfig(PluginConfig):
    name = 'netbox_access_lists'
    verbose_name = ' NetBox Access Lists'
    description = 'Manage simple ACLs in NetBox'
    version = '0.1'
    base_url = 'access-lists'
    min_version = '3.4.0'


config = NetBoxAccessListsConfig

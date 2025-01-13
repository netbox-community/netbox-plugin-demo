from netbox.plugins import PluginConfig

class NetboxOxidizedConfig(PluginConfig):
    name = "netbox_oxidized"
    verbose_name = "NetBox Oxidized"
    description = "Integration with Oxidized to display backups"
    version = "1.0.0"
    base_url = "oxidized"
    default_settings = {}
    required_settings = {}

config = NetboxOxidizedConfig

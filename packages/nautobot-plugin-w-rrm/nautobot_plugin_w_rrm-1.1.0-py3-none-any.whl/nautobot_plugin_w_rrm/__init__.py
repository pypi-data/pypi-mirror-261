# pylint: disable=import-outside-toplevel
"""Plugin declaration for w_rrm."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from django.db.models.signals import post_migrate
from nautobot.extras.plugins import PluginConfig


class WRrmConfig(PluginConfig):
    """Plugin configuration for the nautobot_plugin_w_rrm plugin."""

    name = "nautobot_plugin_w_rrm"
    verbose_name = "Wireless Radio Resource Manager"
    version = __version__
    author = "Hugo Tinoco"
    description = "Wireless Radio Resource Manager."
    base_url = "nautobot-plugin-w-rrm"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {
        "create_roof_location_type": True,
        "circuit_custom_fields": True,
        "core_model_default_statuses": [
            {
                "app": "circuits",
                "model": "Circuit",
                "statuses": ["active", "designed", "rejected", "phase out"],
            }
        ],
        "plugin_model_default_statuses": {
            "RadioAttributes": ["active", "designed", "rejected", "phase out"],
            "CircuitAttributes": ["pending", "cleared"],
        },
    }

    caching_config = {}

    def ready(self):
        """Callback invoked after the plugin is loaded."""
        super().ready()
        from .signals import post_migrate_create_statuses

        post_migrate.connect(post_migrate_create_statuses, sender=self)


config = WRrmConfig  # pylint:disable=invalid-name

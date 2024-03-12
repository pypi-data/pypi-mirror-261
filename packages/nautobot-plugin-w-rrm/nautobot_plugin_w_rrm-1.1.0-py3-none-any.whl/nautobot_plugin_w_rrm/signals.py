"""Nautobot signal handler functions for Nautobot RF Plugin."""

from django.apps import apps as global_apps
from django.conf import settings

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG["nautobot_plugin_w_rrm"]


def post_migrate_create_statuses(sender, *, apps=global_apps, **kwargs):
    """Callback function for post_migrate() -- create default Statuses."""
    # pylint: disable=invalid-name
    if not apps:
        return

    Status = apps.get_model("extras", "Status")

    for model_name, default_statuses in PLUGIN_SETTINGS.get("plugin_model_default_statuses", {}).items():
        model = sender.get_model(model_name)

        ContentType = apps.get_model("contenttypes", "ContentType")
        ct_model = ContentType.objects.get_for_model(model)
        for name in default_statuses:
            status, _ = Status.objects.get_or_create(name=name.capitalize())
            if ct_model not in status.content_types.all():
                status.content_types.add(ct_model)
                status.save()

    if PLUGIN_SETTINGS.get("create_roof_location_type"):
        Device = apps.get_model("dcim", "Device")
        CircuitTermination = apps.get_model("circuits", "CircuitTermination")
        LocationType = apps.get_model("dcim", "LocationType")
        location_type, _ = LocationType.objects.get_or_create(
            name="Roof",
            description="A Roof top on a building.",
            nestable=True,
        )
        for c_type in [
            ContentType.objects.get_for_model(Device),
            ContentType.objects.get_for_model(CircuitTermination),
        ]:
            location_type.content_types.add(c_type)

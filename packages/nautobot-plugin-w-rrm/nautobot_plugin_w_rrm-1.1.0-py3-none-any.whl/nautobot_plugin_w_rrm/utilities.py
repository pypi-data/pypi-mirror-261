"""Utilities."""

from django.contrib.contenttypes.models import ContentType

from nautobot_plugin_w_rrm.models import LocationAttributes


def get_related_location_attributes(object):
    """Determine if the `object` has a relation to LocationAttributes."""
    content_type = ContentType.objects.get_for_model(object)
    related_attributes = LocationAttributes.objects.filter(content_type=content_type, object_id=object.id)
    return related_attributes.first()

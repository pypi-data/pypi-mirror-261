"""API nested serializers for w_rrm."""

from nautobot.core.api import WritableNestedSerializer
from rest_framework import serializers

from nautobot_plugin_w_rrm import models


class RadioAttributesNestedSerializer(WritableNestedSerializer):
    """RadioAttributes Nested Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:nautobot_plugin_w_rrm-api:radioattributes-detail")

    class Meta:
        """Meta attributes."""

        model = models.RadioAttributes
        fields = "__all__"


class LocationAttributesNestedSerializer(WritableNestedSerializer):
    """LocationAttributes Nested Serializer."""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:nautobot_plugin_w_rrm-api:locationattributes-detail"
    )

    class Meta:
        """Meta attributes."""

        model = models.LocationAttributes
        fields = "__all__"


class CircuitAttributesNestedSerializer(WritableNestedSerializer):
    """CircuitAttributes Nested Serializer."""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:nautobot_plugin_w_rrm-api:circuitattributes-detail"
    )

    class Meta:
        """Meta attributes."""

        model = models.CircuitAttributes
        fields = "__all__"

"""API serializers for w_rrm."""

from nautobot.core.api.serializers import ValidatedModelSerializer
from rest_framework import serializers

from nautobot_plugin_w_rrm import models

from . import nested_serializers  # noqa: F401, pylint: disable=unused-import


class RadioAttributesSerializer(ValidatedModelSerializer):
    """RadioAttributes Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:nautobot_plugin_w_rrm-api:radioattributes-detail")

    class Meta:
        """Meta attributes."""

        model = models.RadioAttributes
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []


class LocationAttributesSerializer(ValidatedModelSerializer):
    """LocationAttributes Serializer."""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:nautobot_plugin_w_rrm-api:locationattributes-detail"
    )

    class Meta:
        """Meta attributes."""

        model = models.LocationAttributes
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []


class CircuitAttributesSerializer(ValidatedModelSerializer):
    """CircuitAttributes Serializer."""

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:nautobot_plugin_w_rrm-api:circuitattributes-detail"
    )

    class Meta:
        """Meta attributes."""

        model = models.CircuitAttributes
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []

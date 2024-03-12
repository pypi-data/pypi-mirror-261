"""API views for w_rrm."""

from nautobot.core.api.views import ModelViewSet

from nautobot_plugin_w_rrm import filters, models
from nautobot_plugin_w_rrm.api import serializers


class RadioAttributesViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    """RadioAttributes viewset."""

    queryset = models.RadioAttributes.objects.all()
    serializer_class = serializers.RadioAttributesSerializer
    filterset_class = filters.RadioAttributesFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]


class LocationAttributesViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    """LocationAttributes viewset."""

    queryset = models.LocationAttributes.objects.all()
    serializer_class = serializers.LocationAttributesSerializer
    filterset_class = filters.LocationAttributesFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]


class CircuitAttributesViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    """CircuitAttributes viewset."""

    queryset = models.CircuitAttributes.objects.all()
    serializer_class = serializers.CircuitAttributesSerializer
    filterset_class = filters.CircuitAttributesFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]

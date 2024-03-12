"""Filtering for w_rrm."""

from django.db.models import Q
from django_filters import CharFilter
from nautobot.core.filters import BaseFilterSet

from nautobot_plugin_w_rrm import models


class BaseHumanIdFilterSet(BaseFilterSet):
    """Base filter set to provide a human_id search."""

    q = CharFilter(method="search", label="Search")
    human_id = CharFilter(lookup_expr="iexact")  # Case insensitive exact match

    class Meta:
        """Meta attributes for filter."""

        fields = ["id", "human_id"]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(human_id__icontains=value)
        return queryset.filter(qs_filter)


class RadioAttributesFilterSet(BaseHumanIdFilterSet):
    """Filter for RadioAttributes."""

    class Meta:
        """Meta attributes for filter."""

        model = models.RadioAttributes
        fields = ["id", "human_id"]


class LocationAttributesFilterSet(BaseHumanIdFilterSet):
    """Filter for LocationAttributes."""

    class Meta:
        """Meta attributes for filter."""

        model = models.LocationAttributes

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "ground_height", "roof_height", "latitude", "longitude", "human_id"]


class CircuitAttributesFilterSet(BaseHumanIdFilterSet):
    """Filter for CircuitAttributes."""

    human_id = CharFilter(lookup_expr="iexact")  # Case insensitive exact match

    class Meta:
        """Meta attributes for filter."""

        model = models.CircuitAttributes

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "human_id"]

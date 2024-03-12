# pylint: disable=abstract-method
"""Template Content for nautobot_plugin_w_rrm."""
# from abc import abstractmethod

from django.urls import reverse
from nautobot.extras.plugins import PluginTemplateExtension

from nautobot_plugin_w_rrm.models import CircuitAttributes, RadioAttributes
from nautobot_plugin_w_rrm.utilities import get_related_location_attributes


class DeviceExtraTabs(PluginTemplateExtension):
    """Template extension to add extra tabs to the object detail tabs."""

    model = "dcim.device"

    def detail_tabs(self):
        """
        You may define extra tabs to render on a model's detail page by utilizing this method.

        Each tab is defined as a dict in a list of dicts.

        For each of the tabs defined:
        - The <title> key's value will become the tab link's title.
        - The <url> key's value is used to render the HTML link for the tab

        These tabs will be visible (in this instance) on the Device model's detail page as
        set by the DeviceContent.model attribute "dcim.device"

        This example demonstrates defining two tabs. The tabs will be ordered by their position in list.
        """
        try:
            if self.context["object"].radio_attributes:
                return [
                    {
                        "title": "Radio Attributes",
                        "url": reverse(
                            "plugins:nautobot_plugin_w_rrm:radioattributes",
                            kwargs={"pk": self.context["object"].radio_attributes.pk},
                        ),
                    },
                ]
        except RadioAttributes.DoesNotExist:
            return []


class CircuitExtraTabs(PluginTemplateExtension):
    """Template extension to add extra tabs to the object detail tabs."""

    model = "circuits.circuit"

    def detail_tabs(self):
        """
        You may define extra tabs to render on a model's detail page by utilizing this method.

        Each tab is defined as a dict in a list of dicts.

        For each of the tabs defined:
        - The <title> key's value will become the tab link's title.
        - The <url> key's value is used to render the HTML link for the tab

        These tabs will be visible (in this instance) on the Device model's detail page as
        set by the DeviceContent.model attribute "dcim.device"

        This example demonstrates defining two tabs. The tabs will be ordered by their position in list.
        """
        try:
            if self.context["object"].circuit_attributes:
                return [
                    {
                        "title": "Wireless Circuit Attributes",
                        "url": reverse(
                            "plugins:nautobot_plugin_w_rrm:circuitattributes",
                            kwargs={"pk": self.context["object"].circuit_attributes.get().pk},
                        ),
                    },
                ]
        except CircuitAttributes.DoesNotExist:
            return []


class LocationAttributesLocationExtras(PluginTemplateExtension):
    """Template extension to display animal count on the right side of the page."""

    model = "dcim.location"

    def detail_tabs(self):
        """
        You may define extra tabs to render on a model's detail page by utilizing this method.

        Each tab is defined as a dict in a list of dicts.

        For each of the tabs defined:
        - The <title> key's value will become the tab link's title.
        - The <url> key's value is used to render the HTML link for the tab

        These tabs will be visible (in this instance) on the Device model's detail page as
        set by the DeviceContent.model attribute "dcim.device"

        This example demonstrates defining two tabs. The tabs will be ordered by their position in list.
        """
        related_attributes = get_related_location_attributes(self.context["object"])

        if related_attributes is not None:
            return [
                {
                    "title": "Location Attributes",
                    "url": reverse(
                        "plugins:nautobot_plugin_w_rrm:locationattributes",
                        kwargs={"pk": related_attributes.pk},
                    ),
                },
            ]
        else:
            return []


template_extensions = [
    DeviceExtraTabs,
    CircuitExtraTabs,
    LocationAttributesLocationExtras,
]

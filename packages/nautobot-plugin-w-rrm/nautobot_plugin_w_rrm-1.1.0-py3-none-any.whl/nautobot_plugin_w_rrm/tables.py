"""Tables for w_rrm."""

import django_tables2 as tables
from nautobot.core.tables import BaseTable, ButtonsColumn, ToggleColumn

from nautobot_plugin_w_rrm import models

MANY_RADIOS_TEMPLATE = """
{% for radio in record.radios.all %}
    <a href="{{ radio.get_absolute_url }}">{{ radio }}</a><br />
{% endfor %}
"""


class RadioAttributesTable(BaseTable):
    # pylint: disable=R0903
    """Table for list view."""

    pk = ToggleColumn()
    radio = tables.Column(linkify=True)

    actions = ButtonsColumn(
        models.RadioAttributes,
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        # pk_field="slug",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.RadioAttributes
        fields = ("pk", "radio")

        # Option for modifying the columns that show up in the list view by default:
        # default_columns = (
        #     "pk",
        #     "name",
        #     "description",
        # )


class LocationAttributesTable(BaseTable):
    # pylint: disable=R0903
    """Table for list view."""

    pk = ToggleColumn()
    content_object = tables.Column(empty_values=(), verbose_name="Content Object", linkify=True)
    actions = ButtonsColumn(
        models.LocationAttributes,
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        # pk_field="slug",
    )

    def render_content_object(self, record):
        # return f'{record.content_type.model.capitalize()} {record.object_id}'
        related_object = record.content_object
        return related_object.name if related_object else "None"

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.LocationAttributes
        fields = (
            "pk",
            "content_object",
            "ground_height",
            "roof_height",
            "building_height",
            "latitude",
            "longitude",
        )


class CircuitAttributesTable(BaseTable):
    # pylint: disable=R0903
    """Table for list view."""

    pk = ToggleColumn()
    circuit = tables.Column(linkify=True)
    fcc_status = tables.Column(linkify=True)

    actions = ButtonsColumn(
        models.CircuitAttributes,
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        # pk_field="slug",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.CircuitAttributes
        fields = (
            "pk",
            "circuit",
            "fcc_status",
            "fcc_reference",
            "human_id",
            "order",
            "dl_reliability",
            "ul_reliability",
            "outage",
            "mcs_up",
            "mcs_down",
            "predicted_rx_power_a",
            "predicted_rx_power_z",
            "power_control",
            "description",
            "ssid",
            "rssi_threshold_a_upper",
            "rssi_threshold_a_lower",
            "rssi_threshold_z_upper",
            "rssi_threshold_z_lower",
        )
        default_columns = (
            "pk",
            "circuit",
            "human_id",
            "fcc_status",
            "fcc_reference",
            "order",
            "dl_reliability",
            "ul_reliability",
            "outage",
            "mcs_up",
            "mcs_down",
            "predicted_rx_power_a",
            "predicted_rx_power_z",
            "power_control",
            "description",
        )

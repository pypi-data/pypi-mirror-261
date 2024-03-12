# pylint: disable=too-many-ancestors
"""Models for Wireless Radio Resource Manager."""
# Django imports
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator  # noqa: I001
from django.db import models
from django.urls import reverse

# Nautobot imports
from nautobot.core.models.generics import PrimaryModel
from nautobot.extras.models.statuses import StatusField, StatusModel
from nautobot.extras.utils import extras_features

from nautobot_plugin_w_rrm.constants import (
    CIRCUIT_ORDER_CHOICES,
    LOCATION_ATTRIBUTES_LIMIT_CHOICES,
    POWER_CONTROL_CHOICES,
    RADIO_TYPES_CHOICES,
    TX_HIGH_LOW_CHOICES,
    TX_POLARIZATION_CHOICES,
)

# If you want to use the extras_features decorator please reference the following documentation
# https://nautobot.readthedocs.io/en/latest/plugins/development/#using-the-extras_features-decorator-for-graphql
# Then based on your reading you may decide to put the following decorator before the declaration of your class
# @extras_features("custom_fields", "custom_validators", "relationships", "graphql")


class HumanId(models.Model):
    """Abstract class to provide a human-readable `ID` for a given model instance."""

    human_id = models.CharField(max_length=255, unique=True, editable=True, verbose_name="Human ID")

    class Meta:
        abstract = True


# If you want to choose a specific model to overload in your class declaration,
# please reference the following documentation:
# how to chose a database model: https://nautobot.readthedocs.io/en/stable/plugins/development/#database-models
@extras_features(
    "graphql",
    "relationships",
    "statuses",
)
class RadioAttributes(PrimaryModel, StatusModel, HumanId):
    """RadioAttributes for Wireless Radio Resource Manager plugin."""

    radio_type = models.CharField(max_length=4, choices=RADIO_TYPES_CHOICES, default="PTP")
    description = models.CharField(max_length=200, blank=True, null=True)
    radio = models.OneToOneField(
        to="dcim.Device",
        on_delete=models.PROTECT,
        related_name="radio_attributes",
        verbose_name="Radio",
    )
    failover = models.BooleanField(verbose_name="Failover")
    azimuth = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(359)],
        verbose_name="Azimuth",
    )
    capacity = models.DecimalField(
        blank=True,
        null=True,
        verbose_name="Capacity (Gbs)",
        max_digits=4,
        decimal_places=2,
    )
    is_duplex = models.BooleanField(default=True, verbose_name="Is Duplex")
    tilt = models.IntegerField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)], blank=True, null=True, verbose_name="Tilt"
    )
    centerline_height = models.IntegerField(blank=True, null=True, verbose_name="Centerline Height")
    channel_size = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(8000)],
        verbose_name="Channel Size (MHz)",
    )
    tx_high_low = models.CharField(
        max_length=4, choices=TX_HIGH_LOW_CHOICES, blank=True, null=True, verbose_name="TX High/Low"
    )
    tx_power = models.IntegerField(blank=True, null=True, verbose_name="TX Power (dBm)")
    tx_freq_1 = models.IntegerField(blank=True, null=True, verbose_name="TX Freq 1 (MHz)")
    tx_polarization_1 = models.CharField(
        max_length=4, choices=TX_POLARIZATION_CHOICES, blank=True, null=True, verbose_name="TX Polar 1"
    )
    tx_freq_2 = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="TX Freq 2 (MHz)",
    )
    tx_polarization_2 = models.CharField(
        max_length=4, choices=TX_POLARIZATION_CHOICES, blank=True, verbose_name="TX Polar 2"
    )

    class Meta:
        """Meta class."""

        ordering = ["radio"]
        verbose_name = "Radio Attributes"
        verbose_name_plural = "Radio Attributes"

    def __str__(self):
        """String representation of a RF Radio Attributes."""
        return f"{self.radio} - {self.radio_type} - Radio Attributes"

    def get_absolute_url(self):
        """Return detail view for RadioAttributes."""
        return reverse("plugins:nautobot_plugin_w_rrm:radioattributes", args=[self.pk])


@extras_features(
    "graphql",
    "relationships",
    "statuses",
)
class LocationAttributes(PrimaryModel, HumanId):
    """Location Attributes for W-RRM Plugin."""

    content_type = models.ForeignKey(
        to=ContentType,
        limit_choices_to=LOCATION_ATTRIBUTES_LIMIT_CHOICES,
        on_delete=models.PROTECT,
        related_name="+",
        related_query_name="+",
    )
    object_id = models.UUIDField()
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_id")

    ground_height = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Ground Height (AMSL)",
        default=0,
    )
    roof_height = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Roof Height (AMSL)", default=0)
    building_height = models.PositiveIntegerField(
        validators=[MinValueValidator(0)], verbose_name="Building Height", default=0, editable=False
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[MaxValueValidator(90), MinValueValidator(-90)],
        verbose_name="Latitude",
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[MaxValueValidator(180), MinValueValidator(-180)],
        verbose_name="Longitude",
    )

    class Meta:
        """Meta class."""

        verbose_name = "Location Attributes"
        verbose_name_plural = "Location Attributes"
        unique_together = ("content_type", "object_id")

    def __str__(self):
        """String representation of a Location Attributes."""
        return f"{self.content_object} Attributes"

    def save(self, *args, **kwargs):
        """Save."""
        self.compute_building_height()

        # Ensure only one LocationAttributes is related to a single Location
        if (
            self._state.adding
            and LocationAttributes.objects.filter(content_type=self.content_type, object_id=self.object_id).exists()
        ):
            raise ValidationError(f"LocationAttributes for content_object {self.content_object} already exists.")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return detail view for LocationAttributes."""
        return reverse("plugins:nautobot_plugin_w_rrm:locationattributes", args=[self.pk])

    def compute_building_height(self):
        """
        Compute the building height based on roof_height and ground_height.
        Returns the computed building height.
        """
        if self.ground_height is not None and self.roof_height is not None:
            self.building_height = self.roof_height - self.ground_height
        return self.building_height


@extras_features(
    "graphql",
    "relationships",
    "statuses",
)
class CircuitAttributes(PrimaryModel, HumanId):
    """Circuit Attributes for W-RRM Plugin."""

    circuit = models.ForeignKey("circuits.Circuit", on_delete=models.PROTECT, related_name="circuit_attributes")
    fcc_status = StatusField(
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_related",
        verbose_name="FCC Status",
        null=True,
    )
    fcc_reference = models.CharField(max_length=200, blank=True, null=True, verbose_name="FCC Reference Number")
    order = models.IntegerField("Order", choices=CIRCUIT_ORDER_CHOICES)
    dl_reliability = models.FloatField(verbose_name="DL Reliability (Mbps)")
    ul_reliability = models.FloatField(verbose_name="UL Reliability (Mbps)")
    outage = models.FloatField(verbose_name="Outage (MIN/YR)")
    mcs_up = models.IntegerField(verbose_name="MCS of Uplink", default=0)
    mcs_down = models.IntegerField(verbose_name="MCS of Downlink", default=0)
    predicted_rx_power_a = models.IntegerField(verbose_name="Predicted Rx Power A (dBm)")
    predicted_rx_power_z = models.IntegerField(verbose_name="Predicted Rx Power Z (dBm)")
    power_control = models.CharField(
        "Power Control", max_length=50, blank=True, null=True, choices=POWER_CONTROL_CHOICES
    )
    description = models.CharField(max_length=200, blank=True, null=True)
    ssid = models.CharField(max_length=200, blank=True, null=True, verbose_name="SSID")
    rssi_threshold_a_upper = models.FloatField(
        max_length=200, blank=True, null=True, verbose_name="RSSI Threshold Side A - Upper (dBm)"
    )
    rssi_threshold_a_lower = models.FloatField(
        max_length=200, blank=True, null=True, verbose_name="RSSI Threshold Side A - Lower (dBm)"
    )
    rssi_threshold_z_upper = models.FloatField(
        max_length=200, blank=True, null=True, verbose_name="RSSI Threshold Side B - Upper (dBm)"
    )
    rssi_threshold_z_lower = models.FloatField(
        max_length=200, blank=True, null=True, verbose_name="RSSI Threshold Side B - Lower (dBm)"
    )

    class Meta:
        verbose_name = "Circuit Attributes"
        verbose_name_plural = "Circuit Attributes"
        ordering = ["order"]

    def __str__(self):
        """Stringify instance."""
        return f"{self.circuit} - Wireless Circuit Attributes"

    def save(self, *args, **kwargs):
        self._check_device_attrs()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return detail view for CircuitAttributes."""
        return reverse("plugins:nautobot_plugin_w_rrm:circuitattributes", args=[self.pk])

    def _check_device_attrs(self):
        """Check if `Circuit` attached devices have RadioAttributes. If they do, validate fields."""
        sides = ["a", "z"]
        for side in sides:
            termination_side = f"circuit_termination_{side}"
            termination = getattr(self.circuit, termination_side)
            if termination:
                cable_term_a = getattr(termination.cable, "termination_a")
                if hasattr(cable_term_a, "device"):
                    device = cable_term_a.device
                    if hasattr(device, "radio_attributes"):
                        if not device.radio_attributes.azimuth:
                            raise ValidationError(
                                f"Device: {device.name} doesn't have Azimuth defined under Radio Attributes."
                            )

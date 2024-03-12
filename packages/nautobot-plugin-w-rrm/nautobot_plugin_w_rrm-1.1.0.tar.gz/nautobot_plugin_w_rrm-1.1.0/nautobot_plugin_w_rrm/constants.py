"""Constants."""

from django.db.models import Q

TX_POLARIZATION_CHOICES = (
    ("H", "Horizontal"),
    ("V", "Vertical"),
    ("RHCP", "Right-Hand Circular Polarization"),
    ("LHCP", "Left-Hand Circular Polarization"),
    ("RHEP", "Right-Hand Elliptical Polarization"),
    ("LHEP", "Left-Hand Elliptical Polarization"),
)

RADIO_TYPES_CHOICES = (
    ("PTP", "Point-to-Point"),
    ("PTMP", "Point-to-Multipoint"),
)

TX_HIGH_LOW_CHOICES = (
    ("H", "High"),
    ("L", "Low"),
)

CIRCUIT_ORDER_CHOICES = (
    (1, "Primary"),
    (2, "Secondary"),
    (3, "Tertiary"),
)

POWER_CONTROL_CHOICES = (("ATPC", "ATPC"),)

LOCATION_ATTRIBUTES_LIMIT_CHOICES = Q(app_label="dcim", model__in=("location", "site"))

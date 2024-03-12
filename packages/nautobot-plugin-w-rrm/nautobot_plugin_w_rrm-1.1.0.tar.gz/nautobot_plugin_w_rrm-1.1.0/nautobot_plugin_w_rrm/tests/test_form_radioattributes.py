"""Test radioattributes forms."""

from decimal import Decimal

from django.test import TestCase
from nautobot.core.choices import ColorChoices
from nautobot.dcim.models import (
    Device,
    DeviceType,
    Location,
    LocationType,
    Manufacturer,
)
from nautobot.extras.models import Role
from nautobot.extras.models.statuses import Status

from nautobot_plugin_w_rrm import forms


class RadioAttributesTest(TestCase):
    """Test RadioAttributes forms."""

    def setUp(self):
        """Setup."""
        self.location_type, _ = LocationType.objects.get_or_create(
            name="Site",
            description="A Site.",
            nestable=True,
        )
        self.site, _ = Location.objects.get_or_create(
            name="Building-Y",
            status=Status.objects.get(name="Active"),
            location_type=self.location_type,
        )
        self.manufacturer, _ = Manufacturer.objects.get_or_create(name="Ubiquiti")
        self.device_type, _ = DeviceType.objects.get_or_create(model="Test-DeviceType", manufacturer=self.manufacturer)
        self.role, _ = Role.objects.get_or_create(name="Test-Role", color=ColorChoices.COLOR_RED)
        self.device, _ = Device.objects.get_or_create(
            name="Test-Device-y",
            status=Status.objects.get(name="Active"),
            location=self.site,
            device_type=self.device_type,
            role=self.role,
        )

    def test_specifying_all_fields_success(self):
        form = forms.RadioAttributesForm(
            data={
                "radio_type": "PTP",
                "radio": self.device,
                "failover": False,
                "azimuth": 90,
                "capacity": Decimal("1.5"),
                "is_duplex": True,
                "tilt": 5,
                "centerline_height": 10,
                "channel_size": 20,
                "tx_high_low": "H",
                "tx_power": 100,
                "tx_freq_1": 5200,
                "tx_polarization_1": "H",
                "tx_freq_2": 5200,
                "tx_polarization_2": "V",
                "height": 10,
                "latitude": Decimal("37.7"),
                "longitude": Decimal("-122.4"),
                "status": Status.objects.get(name="Active"),
                "human_id": "Test-Human-ID",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

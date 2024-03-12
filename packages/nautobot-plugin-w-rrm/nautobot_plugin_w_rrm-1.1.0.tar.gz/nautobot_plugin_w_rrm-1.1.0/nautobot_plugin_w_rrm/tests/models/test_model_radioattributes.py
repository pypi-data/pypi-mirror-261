"""Test RadioAttributes."""

from decimal import Decimal

# from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from nautobot_plugin_w_rrm.constants import TX_POLARIZATION_CHOICES
from nautobot_plugin_w_rrm.tests.fixtures import RfFixtures


# pylint: disable=too-many-instance-attributes
class NautobotRFModelTestCase(TestCase):
    """Test Nautobot Utility."""

    def setUp(self):
        """Setup."""
        self.fixtures = RfFixtures()
        self.fixtures.create()

    def test_validations(self):
        """Test validations."""
        self.fixtures.device_a.radio_attributes.full_clean()
        self.fixtures.device_b.radio_attributes.full_clean()

    def test_get_absolute_url(self):
        expected_url = reverse(
            "plugins:nautobot_plugin_w_rrm:radioattributes", args=[self.fixtures.device_a.radio_attributes.pk]
        )
        self.assertEqual(self.fixtures.device_a.radio_attributes.get_absolute_url(), expected_url)

    def test_radio_attributes_creation(self):
        self.assertEqual(self.fixtures.device_a.radio_attributes.radio_type, "PTP")

    def test_radio_attributes_failover(self):
        self.assertEqual(self.fixtures.device_a.radio_attributes.failover, False)

    def test_radio_attributes_azimuth(self):
        self.assertEqual(self.fixtures.device_a.radio_attributes.azimuth, 180)

    def test_radio_attributes_tilt(self):
        self.assertEqual(self.fixtures.device_a.radio_attributes.tilt, 5)

    def test_radio_attributes_tx_power(self):
        self.assertEqual(self.fixtures.device_a.radio_attributes.tx_power, 24)

    def test_radio_attributes_tx_freq_1(self):
        self.assertEqual(self.fixtures.device_a.radio_attributes.tx_freq_1, 5200)

    def test_radio_attributes_tx_polarization_1(self):
        self.assertEqual(self.fixtures.device_a.radio_attributes.tx_polarization_1, TX_POLARIZATION_CHOICES[0][0])

    def test_radio_attributes_tx_freq_2(self):
        self.assertEqual(self.fixtures.device_a.radio_attributes.tx_freq_2, 5800)

    def test_radio_attributes_tx_polarization_2(self):
        self.assertEqual(self.fixtures.device_a.radio_attributes.tx_polarization_2, TX_POLARIZATION_CHOICES[1][0])

    def test_radio_attributes_capacity(self):
        self.assertEqual(self.fixtures.device_a.radio_attributes.capacity, Decimal("1.00"))

    def test_radio_attributes_status(self):
        self.assertEqual(self.fixtures.device_a.radio_attributes.status.name, "Active")

    def test_str(self):
        expected_string = (
            f"{self.fixtures.device_a} - {self.fixtures.device_a.radio_attributes.radio_type} - Radio Attributes"
        )
        self.assertEqual(str(self.fixtures.device_a.radio_attributes), expected_string)

    def test_human_id(self):
        # Check that human_id is created
        self.assertTrue(hasattr(self.fixtures.device_a.radio_attributes, "human_id"))
        self.assertTrue(hasattr(self.fixtures.device_b.radio_attributes, "human_id"))

"""Testing exceptions."""

from django.core.exceptions import ValidationError
from django.test import TestCase

from nautobot_plugin_w_rrm.tests.fixtures import RfFixtures


class CircuitAttributesExceptionsTestCase(TestCase):
    def test_save_with_radio_attributes_without_azimuth(self):
        """Test the save method when the device has radio attributes but no azimuth."""
        with self.assertRaises(ValidationError) as context:
            fixtures = RfFixtures(include_req_radio_attrs=False)
            device_name = fixtures.device_a.name
            fixtures.create()
        error = f"Device: {device_name} doesn't have Azimuth defined under Radio Attributes."
        self.assertTrue(error in str(context.exception))

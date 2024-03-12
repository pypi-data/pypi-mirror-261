import uuid

from django.test import TestCase
from django.urls import reverse
from nautobot.extras.models import Status

from nautobot_plugin_w_rrm.constants import CIRCUIT_ORDER_CHOICES, POWER_CONTROL_CHOICES
from nautobot_plugin_w_rrm.models import CircuitAttributes
from nautobot_plugin_w_rrm.tests.fixtures import RfFixtures


class CircuitAttributesTestCase(TestCase):
    def setUp(self):
        self.fixture = RfFixtures()
        self.fixture.create()

    def test_model_creation(self):
        """Test the creation of CircuitAttributes model."""
        self.assertIsInstance(self.fixture.circuit_attributes, CircuitAttributes)

    def test_model_str(self):
        """Test the __str__ method of CircuitAttributes model."""
        expected_string = f"{self.fixture.circuit} - Wireless Circuit Attributes"
        self.assertEqual(str(self.fixture.circuit_attributes), expected_string)

    def test_model_absolute_url(self):
        """Test the get_absolute_url method of CircuitAttributes model."""
        expected_url = reverse(
            "plugins:nautobot_plugin_w_rrm:circuitattributes", args=[self.fixture.circuit_attributes.pk]
        )
        self.assertEqual(self.fixture.circuit_attributes.get_absolute_url(), expected_url)

    def test_ordering(self):
        """Test the ordering of CircuitAttributes model."""
        circuit_attribute_1 = CircuitAttributes.objects.create(
            human_id=f"C-{uuid.uuid4()}",
            circuit=self.fixture.circuit,
            fcc_status=Status.objects.get(name="Cleared"),
            fcc_reference="FCCREF12345",
            order=CIRCUIT_ORDER_CHOICES[0][0],
            dl_reliability=99.99,
            ul_reliability=99.99,
            outage=0.1,
            mcs_up=16,
            mcs_down=16,
            predicted_rx_power_a=-50,
            predicted_rx_power_z=-50,
            power_control=POWER_CONTROL_CHOICES[0][0],
            description="Attributes for circuit between Building A and B",
            rssi_threshold_a_upper="-48",
            rssi_threshold_a_lower="-52",
            rssi_threshold_z_upper="-48",
            rssi_threshold_z_lower="-52",
        )
        self.assertEqual(circuit_attribute_1.order, 1)
        self.assertEqual(circuit_attribute_1.rssi_threshold_a_upper, "-48")

        circuit_attribute_2 = CircuitAttributes.objects.create(
            human_id=f"C-{uuid.uuid4()}",
            circuit=self.fixture.circuit,
            fcc_status=Status.objects.get(name="Cleared"),
            fcc_reference="FCCREF12346",
            dl_reliability=99.99,
            ul_reliability=99.99,
            outage=0.1,
            mcs_up=16,
            mcs_down=16,
            predicted_rx_power_a=-50,
            predicted_rx_power_z=-50,
            power_control=POWER_CONTROL_CHOICES[0][0],
            description="Attributes for circuit between Building A and B",
            order=CIRCUIT_ORDER_CHOICES[1][0],
        )
        self.assertEqual(circuit_attribute_2.order, 2)
        self.assertEqual(circuit_attribute_2.rssi_threshold_a_upper, None)

"""Create fixtures for tests."""

import uuid
from dataclasses import dataclass
from decimal import Decimal

from django.contrib.contenttypes.models import ContentType
from nautobot.circuits.choices import CircuitTerminationSideChoices
from nautobot.circuits.models import Circuit, CircuitTermination, CircuitType, Provider
from nautobot.core.choices import ColorChoices
from nautobot.dcim.choices import InterfaceTypeChoices
from nautobot.dcim.models import (
    Cable,
    Device,
    DeviceType,
    Interface,
    Location,
    LocationType,
    Manufacturer,
)
from nautobot.extras.models import Role
from nautobot.extras.models.statuses import Status

from nautobot_plugin_w_rrm.constants import (
    CIRCUIT_ORDER_CHOICES,
    POWER_CONTROL_CHOICES,
    RADIO_TYPES_CHOICES,
    TX_HIGH_LOW_CHOICES,
    TX_POLARIZATION_CHOICES,
)
from nautobot_plugin_w_rrm.models import (
    CircuitAttributes,
    LocationAttributes,
    RadioAttributes,
)


@dataclass
class RfFixtures:
    """Create required objects for devices."""

    device_a: Device = None
    device_b: Device = None
    location_a: Location = None
    location_b: Location = None
    location_type: LocationType = None
    circuit: Circuit = None
    circuit_type: CircuitType = None
    provider: Provider = None
    termination_a: CircuitTermination = None
    termination_b: CircuitTermination = None
    location_type: LocationType = None
    location: Location = None
    provider_1: Provider = None
    provider_2: Provider = None
    circuit_attributes: CircuitAttributes = None
    include_req_radio_attrs: bool = True

    def __post_init__(self):
        # Get the ContentType for the Device model
        self.provider, _ = Provider.objects.get_or_create(name="Provider Y")
        self.circuit_type, _ = CircuitType.objects.get_or_create(name="Wireless Link")
        device_content_type = ContentType.objects.get_for_model(Device)
        circuit_content_type = ContentType.objects.get_for_model(CircuitTermination)
        self.location_type, _ = LocationType.objects.get_or_create(
            name="Roof",
            description="A Roof top on a building.",
            nestable=True,
        )
        for c_type in [circuit_content_type, device_content_type]:
            self.location_type.content_types.add(c_type)
        self.location_type.save()
        self.site_a, _ = Location.objects.get_or_create(
            name="Building-A",
            status=Status.objects.get(name="Active"),
            location_type=self.location_type,
        )
        self.location_a, _ = Location.objects.get_or_create(
            name="Roof Top A",
            parent=self.site_a,
            location_type=self.location_type,
            status=Status.objects.get(name="Active"),
        )
        self.site_b, _ = Location.objects.get_or_create(
            name="Building-B",
            status=Status.objects.get(name="Active"),
            location_type=self.location_type,
        )
        self.location_b, _ = Location.objects.get_or_create(
            name="Roof Top B",
            parent=self.site_b,
            location_type=self.location_type,
            status=Status.objects.get(name="Active"),
        )
        self.manufacturer, _ = Manufacturer.objects.get_or_create(name="Ubiquiti")
        self.device_type, _ = DeviceType.objects.get_or_create(model="Test-DeviceType", manufacturer=self.manufacturer)
        self.role, _ = Role.objects.get_or_create(name="Test-Role", color=ColorChoices.COLOR_RED)
        self.device_a, _ = Device.objects.get_or_create(
            name="Test-Device-A",
            status=Status.objects.get(name="Active"),
            location=self.location_a,
            device_type=self.device_type,
            role=self.role,
        )
        self.device_b, _ = Device.objects.get_or_create(
            name="Test-Device-B",
            status=Status.objects.get(name="Active"),
            location=self.location_b,
            device_type=self.device_type,
            role=self.role,
        )

        self.location_type_1, _ = LocationType.objects.get_or_create(name="RoofTop")
        self.location_1, _ = Location.objects.get_or_create(
            name="Location 1",
            location_type=self.location_type_1,
            parent=self.site_a,
            status=Status.objects.get(name="Active"),
        )
        self.location_2, _ = Location.objects.get_or_create(
            name="Location 2",
            location_type=self.location_type_1,
            parent=self.site_b,
            status=Status.objects.get(name="Active"),
        )
        self.provider_1, _ = Provider.objects.get_or_create(name="Provider 1")
        self.provider_2, _ = Provider.objects.get_or_create(name="Provider 2")

    def create(self):
        """Fixture to create necessary number of RadioAttributes for tests."""

        for device in [self.device_a, self.device_b]:
            if self.include_req_radio_attrs:
                RadioAttributes.objects.get_or_create(
                    human_id=f"R-{uuid.uuid4()}",
                    radio_type=RADIO_TYPES_CHOICES[0][0],
                    radio=device,
                    description="Some Note",
                    failover=False,
                    azimuth=180,
                    tilt=5,
                    centerline_height=100,
                    channel_size=2160,
                    tx_high_low=TX_HIGH_LOW_CHOICES[0][0],
                    tx_power=24,
                    tx_freq_1=5200,
                    tx_polarization_1=TX_POLARIZATION_CHOICES[0][0],
                    tx_freq_2=5800,
                    tx_polarization_2=TX_POLARIZATION_CHOICES[1][0],
                    capacity=Decimal("1.0"),
                    status=Status.objects.get(name="Active"),
                )
            else:
                RadioAttributes.objects.get_or_create(
                    human_id=f"R-{uuid.uuid4()}",
                    radio_type=RADIO_TYPES_CHOICES[0][0],
                    radio=device,
                    failover=False,
                    description="Some Note",
                    tilt=5,
                    centerline_height=100,
                    channel_size=2160,
                    tx_high_low=TX_HIGH_LOW_CHOICES[0][0],
                    tx_power=24,
                    tx_freq_1=5200,
                    tx_polarization_1=TX_POLARIZATION_CHOICES[0][0],
                    tx_freq_2=5800,
                    tx_polarization_2=TX_POLARIZATION_CHOICES[1][0],
                    capacity=Decimal("1.0"),
                    status=Status.objects.get(name="Active"),
                )
            Interface.objects.get_or_create(
                device=device,
                name="WLAN-0",
                type=InterfaceTypeChoices.TYPE_OTHER_WIRELESS,
                status=Status.objects.get(name="Active"),
            )
        # Create a new Circuit

        self.circuit, _ = Circuit.objects.get_or_create(
            cid="RF12345",  # replace with your circuit ID
            provider=self.provider,
            circuit_type=self.circuit_type,
            status=Status.objects.get(name="Active"),
            description="Wireless Link between Building A and Building B",
        )
        # Create two CircuitTerminations and associate them with the Circuit
        # Here we're associating the terminations with the Device and the Location

        self.termination_a, _ = CircuitTermination.objects.get_or_create(
            circuit=self.circuit,
            term_side=CircuitTerminationSideChoices.SIDE_A,
            location=self.location_a,
            description="Wireless Link to Building A",
        )
        self.termination_a.validated_save()
        self.termination_b, _ = CircuitTermination.objects.get_or_create(
            circuit=self.circuit,
            term_side=CircuitTerminationSideChoices.SIDE_Z,
            location=self.location_b,
            description="Wireless Link to Building B",
        )
        self.termination_b.validated_save()
        # Cables
        self.status = Status.objects.get_for_model(Cable).get(name="Connected")
        cables = [
            {
                "termination": self.termination_a,
                "interface": Interface.objects.get(
                    device=self.device_a, status=Status.objects.get(name="Active"), name="WLAN-0"
                ),
            },
            {
                "termination": self.termination_b,
                "interface": Interface.objects.get(
                    device=self.device_b, status=Status.objects.get(name="Active"), name="WLAN-0"
                ),
            },
        ]
        for cable in cables:
            try:
                self.cable = Cable(
                    termination_a=cable["interface"],
                    termination_b=cable["termination"],
                    status=self.status,
                )
                self.cable.save()
            except Exception as error:
                print("Error creating cables! Perhaps they are already present. %s", error)

        content_type = ContentType.objects.get_for_model(self.location_a)
        self.location_attribute_1, _ = LocationAttributes.objects.get_or_create(
            human_id=f"L-{uuid.uuid4()}",
            content_type=content_type,
            object_id=self.location_a.id,
            ground_height=10,
            roof_height=20,
            latitude=Decimal("12.971598"),
            longitude=Decimal("77.594562"),
        )
        content_type = ContentType.objects.get_for_model(self.location_b)
        self.location_attribute_2, _ = LocationAttributes.objects.get_or_create(
            human_id=f"L-{uuid.uuid4()}",
            content_type=content_type,
            object_id=self.location_b.id,
            ground_height=44,
            roof_height=50,
            latitude=Decimal("18.971598"),
            longitude=Decimal("70.594562"),
        )
        self.circuit_attributes, _ = CircuitAttributes.objects.get_or_create(
            human_id=f"C-{uuid.uuid4()}",
            circuit=self.circuit,
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
        self.circuit_attributes.validated_save()

"""Tests for LocationAttributes model."""

import uuid
from decimal import Decimal

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from nautobot.circuits.models import Provider
from nautobot.dcim.models import Location, LocationType
from nautobot.extras.models.statuses import Status

from nautobot_plugin_w_rrm.models import LocationAttributes


class LocationAttributesTestCase(TestCase):
    """LocationAttributes model tests."""

    def setUp(self):
        # Setting up Providers
        self.provider_1 = Provider.objects.create(name="Provider 1")
        self.provider_2 = Provider.objects.create(name="Provider 2")

        # Setting up LocationType
        self.location_type_1 = LocationType.objects.create(name="RoofTop")
        self.location_type_site, _ = LocationType.objects.get_or_create(
            name="Site",
            description="A Site.",
            nestable=True,
        )
        # Setting up Site
        self.site_1 = Location.objects.create(
            name="Site 1", status=Status.objects.get(name="Active"), location_type=self.location_type_site
        )

        # Setting up Location
        self.location = Location.objects.create(
            name="Location 1",
            location_type=self.location_type_1,
            parent=self.site_1,
            status=Status.objects.get(name="Active"),
        )
        location_content_type = ContentType.objects.get_for_model(Location)
        site_content_type = ContentType.objects.get_for_model(Location)
        # Setting up LocationAttributes
        # TODO
        self.location_attribute_1 = LocationAttributes.objects.create(
            human_id=f"L-{uuid.uuid4()}",
            content_type=location_content_type,
            object_id=self.location.pk,
            ground_height=10,
            roof_height=20,
            latitude=Decimal("12.971598"),
            longitude=Decimal("77.594562"),
        )

        self.location_attribute_2 = LocationAttributes.objects.create(
            human_id=f"L-{uuid.uuid4()}",
            content_type=site_content_type,
            object_id=self.site_1.pk,
            ground_height=10,
            roof_height=20,
            latitude=Decimal("12.971598"),
            longitude=Decimal("77.594562"),
        )

    def test_location_attribute_location(self):
        """Test a basic location attribute creation"""
        self.assertEqual(
            self.location_attribute_1.object_id,
            self.location.pk,
        )

    def test_location_attribute_site(self):
        """Test a basic location attribute creation"""
        self.assertEqual(
            self.location_attribute_2.object_id,
            self.site_1.pk,
        )

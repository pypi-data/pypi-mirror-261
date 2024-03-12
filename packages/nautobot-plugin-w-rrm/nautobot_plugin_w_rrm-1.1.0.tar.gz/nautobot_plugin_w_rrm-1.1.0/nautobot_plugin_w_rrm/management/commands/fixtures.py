"""Management command to bootstrap dummy data for RF model plugin."""

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from nautobot_plugin_w_rrm.tests.fixtures import RfFixtures


class Command(BaseCommand):
    """Publish command to bootstrap dummy data."""

    def handle(self, *args, **options):
        """Publish command to bootstrap dummy data."""
        self.stdout.write("Attempting to populate dummy data.")
        try:
            data = RfFixtures()
            data.create()
            self.stdout.write(self.style.SUCCESS("Successfully populated dummy data!"))
        except IntegrityError as error:
            self.stdout.write(self.style.ERROR(f"Unable to populate data \n {error}"))

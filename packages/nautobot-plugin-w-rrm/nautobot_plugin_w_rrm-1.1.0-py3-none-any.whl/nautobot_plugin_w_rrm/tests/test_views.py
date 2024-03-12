# """Unit tests for views."""
# from nautobot.utilities.testing import ViewTestCases

# from nautobot_plugin_w_rrm import models
# from nautobot_plugin_w_rrm.tests import fixtures


# class RadioAttributesViewTest(ViewTestCases.PrimaryObjectViewTestCase):
#     # pylint: disable=too-many-ancestors
#     """Test the RadioAttributes views."""

#     model = models.RadioAttributes
#     bulk_edit_data = {"description": "Bulk edit views"}
#     form_data = {
#         "name": "Test 1",
#         "slug": "test-1",
#         "description": "Initial model",
#     }

#     @classmethod
#     def setUpTestData(cls):
#         fixtures.create_radioattributes()

#     def test_bulk_import_objects_with_constrained_permission(self):
#         pass

#     def test_bulk_import_objects_with_permission(self):
#         pass

#     def test_bulk_import_objects_without_permission(self):
#         pass


# class LocationAttributesViewTest(ViewTestCases.PrimaryObjectViewTestCase):
#     # pylint: disable=too-many-ancestors
#     """Test the LocationAttributes views."""

#     model = models.LocationAttributes
#     bulk_edit_data = {"description": "Bulk edit views"}
#     form_data = {
#         "name": "Test 1",
#         "slug": "test-1",
#         "description": "Initial model",
#     }

#     @classmethod
#     def setUpTestData(cls):
#         fixtures.create_locationattributes()

#     def test_bulk_import_objects_with_constrained_permission(self):
#         pass

#     def test_bulk_import_objects_with_permission(self):
#         pass

#     def test_bulk_import_objects_without_permission(self):
#         pass

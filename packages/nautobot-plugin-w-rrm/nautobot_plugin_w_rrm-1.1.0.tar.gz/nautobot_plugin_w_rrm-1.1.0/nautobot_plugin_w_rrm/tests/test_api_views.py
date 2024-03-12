# """Unit tests for w_rrm."""
# from nautobot.utilities.testing import APIViewTestCases

# from nautobot_plugin_w_rrm import models
# from nautobot_plugin_w_rrm.tests import fixtures


# class RadioAttributesAPIViewTest(APIViewTestCases.APIViewTestCase):
#     # pylint: disable=too-many-ancestors
#     """Test the API viewsets for RadioAttributes."""

#     model = models.RadioAttributes
#     create_data = [
#         {
#             "name": "Test Model 1",
#             "slug": "test-model-1",
#         },
#         {
#             "name": "Test Model 2",
#             "slug": "test-model-2",
#         },
#     ]
#     bulk_update_data = {"description": "Test Bulk Update"}
#     brief_fields = ["created", "description", "display", "id", "last_updated", "name", "slug", "url"]

#     @classmethod
#     def setUpTestData(cls):
#         fixtures.create_radioattributes()

# class LocationAttributesAPIViewTest(APIViewTestCases.APIViewTestCase):
#     # pylint: disable=too-many-ancestors
#     """Test the API viewsets for LocationAttributes."""

# model = models.LocationAttributes
# create_data = [
#     {
#         "name": "Test Model 1",
#         "slug": "test-model-1",
#     },
#     {
#         "name": "Test Model 2",
#         "slug": "test-model-2",
#     },
# ]
# bulk_update_data = {"description": "Test Bulk Update"}
# brief_fields = ["created", "description", "display", "id", "last_updated", "name", "slug", "url"]

# @classmethod
# def setUpTestData(cls):
#     fixtures.create_locationattributes()

# """Test LocationAttributes Filter."""
# from django.test import TestCase

# from nautobot_plugin_w_rrm import filters, models
# from nautobot_plugin_w_rrm.tests import fixtures


# class LocationAttributesFilterTestCase(TestCase):
#     """LocationAttributes Filter Test Case."""

#     queryset = models.LocationAttributes.objects.all()
#     filterset = filters.LocationAttributesFilterSet

#     @classmethod
#     def setUpTestData(cls):
#         """Setup test data for LocationAttributes Model."""
#         fixtures.create_locationattributes()

#     def test_q_search_name(self):
#         """Test using Q search with name of LocationAttributes."""
#         params = {"q": "Test One"}
#         self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

#     def test_q_search_slug(self):
#         """Test using Q search with slug of LocationAttributes."""
#         params = {"q": "test-one"}
#         self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

#     def test_q_invalid(self):
#         """Test using invalid Q search for LocationAttributes."""
#         params = {"q": "test-five"}
#         self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)

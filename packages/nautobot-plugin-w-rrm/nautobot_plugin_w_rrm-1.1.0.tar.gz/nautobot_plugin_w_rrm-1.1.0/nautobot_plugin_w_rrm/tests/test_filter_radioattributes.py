# """Test RadioAttributes Filter."""
# from django.test import TestCase

# from nautobot_plugin_w_rrm import filters, models
# from nautobot_plugin_w_rrm.tests import fixtures


# class RadioAttributesFilterTestCase(TestCase):
#     """RadioAttributes Filter Test Case."""

#     queryset = models.RadioAttributes.objects.all()
#     filterset = filters.RadioAttributesFilterSet

#     @classmethod
#     def setUpTestData(cls):
#         """Setup test data for RadioAttributes Model."""
#         fixtures.create_radioattributes()

#     def test_q_search_name(self):
#         """Test using Q search with name of RadioAttributes."""
#         params = {"q": "Test One"}
#         self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

#     def test_q_search_slug(self):
#         """Test using Q search with slug of RadioAttributes."""
#         params = {"q": "test-one"}
#         self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

#     def test_q_invalid(self):
#         """Test using invalid Q search for RadioAttributes."""
#         params = {"q": "test-five"}
#         self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)

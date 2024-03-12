# """Test locationattributes forms."""
# from django.test import TestCase

# from nautobot_plugin_w_rrm import forms


# class LocationAttributesTest(TestCase):
#     """Test LocationAttributes forms."""

#     def test_specifying_all_fields_success(self):
#         form = forms.LocationAttributesForm(
#             data={
#                 "name": "Development",
#                 "slug": "development",
#                 "description": "Development Testing",
#             }
#         )
#         self.assertTrue(form.is_valid())
#         self.assertTrue(form.save())

#     def test_specifying_only_required_success(self):
#         form = forms.LocationAttributesForm(
#             data={
#                 "name": "Development",
#                 "slug": "development",
#             }
#         )
#         self.assertTrue(form.is_valid())
#         self.assertTrue(form.save())

#     def test_validate_name_locationattributes_is_required(self):
#         form = forms.LocationAttributesForm(data={"slug": "development"})
#         self.assertFalse(form.is_valid())
#         self.assertIn("This field is required.", form.errors["name"])

#     def test_validate_slug_is_required(self):
#         form = forms.LocationAttributesForm(data={"name": "Development"})
#         self.assertFalse(form.is_valid())
#         self.assertIn("This field is required.", form.errors["slug"])

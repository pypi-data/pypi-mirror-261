"""Forms for w_rrm."""

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError

# from nautobot.extras.models import Status
from nautobot.core.forms import BootstrapMixin, BulkEditForm, DynamicModelChoiceField
from nautobot.dcim.models import Device, Location
from nautobot.extras.forms import (
    RelationshipModelForm,
    StatusBulkEditFormMixin,
    StatusFilterFormMixin,
)

from nautobot_plugin_w_rrm.models import (
    CircuitAttributes,
    LocationAttributes,
    RadioAttributes,
)


class RadioAttributesForm(BootstrapMixin, RelationshipModelForm):
    """RadioAttributes creation/edit form."""

    model = RadioAttributes
    radio = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)

    class Meta:
        """Meta attributes."""

        model = RadioAttributes
        fields = [
            "radio",
            "human_id",
            "status",
            "capacity",
            "is_duplex",
            "failover",
            "azimuth",
            "tilt",
            "centerline_height",
            "channel_size",
            "tx_high_low",
            "tx_power",
            "tx_freq_1",
            "tx_polarization_1",
            "tx_freq_2",
            "tx_polarization_2",
        ]


class RadioAttributesBulkEditForm(BootstrapMixin, BulkEditForm, RelationshipModelForm, StatusBulkEditFormMixin):
    """RadioAttributes bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=RadioAttributes.objects.all(), widget=forms.MultipleHiddenInput)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "radio",
        ]


class RadioAttributesFilterForm(BootstrapMixin, RelationshipModelForm, StatusFilterFormMixin):
    """Filter form to filter searches."""

    model = RadioAttributes

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )

    class Meta:
        """Meta attributes."""

        model = RadioAttributes
        # Define the fields above for ordering and widget purposes
        fields = [
            "q",
        ]


class LocationAttributesForm(BootstrapMixin, forms.ModelForm):
    """LocationAttributes creation/edit form."""

    model = LocationAttributes
    location = DynamicModelChoiceField(queryset=Location.objects.all(), label="Location", required=False)

    class Meta:
        """Meta attributes."""

        model = LocationAttributes
        fields = (
            "ground_height",
            "roof_height",
            "latitude",
            "longitude",
        )

    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get("location")

        if location:
            content_type = ContentType.objects.get_for_model(Location)
            if LocationAttributes.objects.filter(content_type=content_type, object_id=location.pk).exists():
                raise ValidationError("The selected location is already associated with another LocationAttribute.")

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.content_type = ContentType.objects.get_for_model(Location)
        instance.object_id = self.cleaned_data["location"].pk
        if commit:
            instance.save()
        return instance


class LocationAttributesBulkEditForm(BootstrapMixin, BulkEditForm):
    """LocationAttributes bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=LocationAttributes.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class LocationAttributesFilterForm(BootstrapMixin, forms.ModelForm):
    """Filter form to filter searches."""

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )

    class Meta:
        """Meta attributes."""

        model = LocationAttributes
        # Define the fields above for ordering and widget purposes
        fields = [
            "q",
        ]


class CircuitAttributesForm(BootstrapMixin, forms.ModelForm):
    """CircuitAttributes creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = CircuitAttributes
        fields = [
            "fcc_status",
            "human_id",
            "description",
            "circuit",
            "fcc_reference",
            "order",
            "dl_reliability",
            "ul_reliability",
            "outage",
            "mcs_up",
            "mcs_down",
            "predicted_rx_power_a",
            "predicted_rx_power_z",
            "power_control",
            "ssid",
            "rssi_threshold_a_upper",
            "rssi_threshold_a_lower",
            "rssi_threshold_z_upper",
            "rssi_threshold_z_lower",
        ]

    def clean(self):
        """Clean and validate the form data."""
        cleaned_data = super().clean()

        circuit = cleaned_data.get("circuit")
        if circuit:
            sides = ["a", "z"]
            for side in sides:
                termination_side = f"termination_{side}"
                termination = getattr(circuit, termination_side)
                if termination:
                    cable_term_a = getattr(termination.cable, "termination_a")
                    if hasattr(cable_term_a, "device"):
                        device = cable_term_a.device
                        if hasattr(device, "radio_attributes"):
                            if not device.radio_attributes.azimuth:
                                self.add_error(
                                    None,
                                    ValidationError(
                                        f"Device: {device.name} doesn't have Azimuth defined under Radio Attributes."
                                    ),
                                )

        return cleaned_data


class CircuitAttributesBulkEditForm(BootstrapMixin, BulkEditForm):
    """CircuitAttributes bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=CircuitAttributes.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class CircuitAttributesFilterForm(BootstrapMixin, forms.ModelForm):
    """Filter form to filter searches."""

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )

    class Meta:
        """Meta attributes."""

        model = CircuitAttributes
        # Define the fields above for ordering and widget purposes
        fields = [
            "q",
            "description",
        ]

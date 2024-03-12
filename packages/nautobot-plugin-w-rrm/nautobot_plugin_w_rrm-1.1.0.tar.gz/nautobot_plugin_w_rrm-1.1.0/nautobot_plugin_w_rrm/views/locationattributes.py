"""Views for LocationAttributes."""

from nautobot.core.views import generic

from nautobot_plugin_w_rrm import filters, forms, models, tables


class LocationAttributesListView(generic.ObjectListView):
    """List view."""

    queryset = models.LocationAttributes.objects.all()
    # These aren't needed for simple models, but we can always add
    # this search functionality.
    filterset = filters.LocationAttributesFilterSet
    filterset_form = forms.LocationAttributesFilterForm
    table = tables.LocationAttributesTable

    # Option for modifying the top right buttons on the list view:
    # action_buttons = ("add", "import", "export")


class LocationAttributesView(generic.ObjectView):
    """Detail view."""

    queryset = models.LocationAttributes.objects.all()


class LocationAttributesCreateView(generic.ObjectEditView):
    """Create view."""

    model = models.LocationAttributes
    queryset = models.LocationAttributes.objects.all()
    model_form = forms.LocationAttributesForm


class LocationAttributesDeleteView(generic.ObjectDeleteView):
    """Delete view."""

    model = models.LocationAttributes
    queryset = models.LocationAttributes.objects.all()


class LocationAttributesEditView(generic.ObjectEditView):
    """Edit view."""

    model = models.LocationAttributes
    queryset = models.LocationAttributes.objects.all()
    model_form = forms.LocationAttributesForm


class LocationAttributesBulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more LocationAttributes records."""

    queryset = models.LocationAttributes.objects.all()
    table = tables.LocationAttributesTable


class LocationAttributesBulkEditView(generic.BulkEditView):
    """View for editing one or more LocationAttributes records."""

    queryset = models.LocationAttributes.objects.all()
    table = tables.LocationAttributesTable
    form = forms.LocationAttributesBulkEditForm

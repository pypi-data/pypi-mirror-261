"""Views for RadioAttributes."""

from nautobot.core.views import generic

from nautobot_plugin_w_rrm import filters, forms, models, tables


class RadioAttributesListView(generic.ObjectListView):
    """List view."""

    queryset = models.RadioAttributes.objects.all()
    # These aren't needed for simple models, but we can always add
    # this search functionality.
    filterset = filters.RadioAttributesFilterSet
    filterset_form = forms.RadioAttributesFilterForm
    table = tables.RadioAttributesTable
    # Option for modifying the top right buttons on the list view:
    # action_buttons = ("add", "import", "export")


class RadioAttributesView(generic.ObjectView):
    """Detail view."""

    queryset = models.RadioAttributes.objects.all()


class RadioAttributesCreateView(generic.ObjectEditView):
    """Create view."""

    model = models.RadioAttributes
    queryset = models.RadioAttributes.objects.all()
    model_form = forms.RadioAttributesForm


class RadioAttributesDeleteView(generic.ObjectDeleteView):
    """Delete view."""

    model = models.RadioAttributes
    queryset = models.RadioAttributes.objects.all()


class RadioAttributesEditView(generic.ObjectEditView):
    """Edit view."""

    model = models.RadioAttributes
    queryset = models.RadioAttributes.objects.all()
    model_form = forms.RadioAttributesForm


class RadioAttributesBulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more RadioAttributes records."""

    queryset = models.RadioAttributes.objects.all()
    table = tables.RadioAttributesTable


class RadioAttributesBulkEditView(generic.BulkEditView):
    """View for editing one or more RadioAttributes records."""

    queryset = models.RadioAttributes.objects.all()
    table = tables.RadioAttributesTable
    form = forms.RadioAttributesBulkEditForm

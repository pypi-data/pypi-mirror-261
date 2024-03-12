"""Views for CircuitAttributes."""

from datetime import timedelta
from io import BytesIO

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from django.utils import timezone
from nautobot.core.views import generic
from xhtml2pdf import pisa

from nautobot_plugin_w_rrm import filters, forms, models, tables


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return result.getvalue()
    return None


class CircuitRfds(generic.ObjectView):
    """Detail view for CircuitAttributes that provides a PDF export."""

    queryset = models.CircuitAttributes.objects.all()
    template_name = "nautobot_plugin_w_rrm/circuitrfds.html"

    def get_rfds_info(self, object) -> dict:
        now = timezone.now()
        future_date = now + timedelta(days=30)
        return {"now": now, "future_date": future_date}

    def get_context_data(self, **kwargs):
        context = {
            **kwargs,
        }
        context.update(self.get_rfds_info(kwargs.get("object")))
        return context

    def render_to_response(self, context, **response_kwargs):
        instance = context["object"]
        pdf = render_to_pdf(
            self.template_name,
            context,
        )
        if pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            filename = f"CircuitAttributes_{instance.human_id}.pdf"
            content = "attachment; filename='%s'" % (filename)
            response["Content-Disposition"] = content
            return response
        return HttpResponse("Not found")

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(self.queryset, **kwargs)
        context = self.get_context_data(object=instance, request=request, settings=settings)
        context.update(
            {
                "object": instance,
                "verbose_name": self.queryset.model._meta.verbose_name,
                "verbose_name_plural": self.queryset.model._meta.verbose_name_plural,
            }
        )

        if "pdf" in request.GET:
            return self.render_to_response(context, **kwargs)
        return render(request, self.template_name, context)


class CircuitAttributesListView(generic.ObjectListView):
    """List view."""

    queryset = models.CircuitAttributes.objects.all()
    # These aren't needed for simple models, but we can always add
    # this search functionality.
    filterset = filters.CircuitAttributesFilterSet
    filterset_form = forms.CircuitAttributesFilterForm
    table = tables.CircuitAttributesTable

    # Option for modifying the top right buttons on the list view:
    # action_buttons = ("add", "import", "export")


class CircuitAttributesView(generic.ObjectView):
    """Detail view."""

    queryset = models.CircuitAttributes.objects.all()


class CircuitAttributesCreateView(generic.ObjectEditView):
    """Create view."""

    model = models.CircuitAttributes
    queryset = models.CircuitAttributes.objects.all()
    model_form = forms.CircuitAttributesForm


class CircuitAttributesDeleteView(generic.ObjectDeleteView):
    """Delete view."""

    model = models.CircuitAttributes
    queryset = models.CircuitAttributes.objects.all()


class CircuitAttributesEditView(generic.ObjectEditView):
    """Edit view."""

    model = models.CircuitAttributes
    queryset = models.CircuitAttributes.objects.all()
    model_form = forms.CircuitAttributesForm


class CircuitAttributesBulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more CircuitAttributes records."""

    queryset = models.CircuitAttributes.objects.all()
    table = tables.CircuitAttributesTable


class CircuitAttributesBulkEditView(generic.BulkEditView):
    """View for editing one or more CircuitAttributes records."""

    queryset = models.CircuitAttributes.objects.all()
    table = tables.CircuitAttributesTable
    form = forms.CircuitAttributesBulkEditForm

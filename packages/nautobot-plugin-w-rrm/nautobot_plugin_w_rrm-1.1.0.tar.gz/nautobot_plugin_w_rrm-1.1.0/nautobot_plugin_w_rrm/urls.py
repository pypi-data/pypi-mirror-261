"""Django urlpatterns declaration for w_rrm plugin."""

from django.urls import path
from nautobot.extras.views import ObjectChangeLogView

from nautobot_plugin_w_rrm import models
from nautobot_plugin_w_rrm.views import (
    circuitattributes,
    locationattributes,
    rfattributes_views,
)

urlpatterns = [
    # RadioAttributes URLs
    path("radioattributes/", rfattributes_views.RadioAttributesListView.as_view(), name="radioattributes_list"),
    # Order is important for these URLs to work (add/delete/edit) to be before any that require uuid/slug
    path("radioattributes/add/", rfattributes_views.RadioAttributesCreateView.as_view(), name="radioattributes_add"),
    path(
        "radioattributes/delete/",
        rfattributes_views.RadioAttributesBulkDeleteView.as_view(),
        name="radioattributes_bulk_delete",
    ),
    path(
        "radioattributes/edit/",
        rfattributes_views.RadioAttributesBulkEditView.as_view(),
        name="radioattributes_bulk_edit",
    ),
    path("radioattributes/<uuid:pk>/", rfattributes_views.RadioAttributesView.as_view(), name="radioattributes"),
    path(
        "radioattributes/<uuid:pk>/delete/",
        rfattributes_views.RadioAttributesDeleteView.as_view(),
        name="radioattributes_delete",
    ),
    path(
        "radioattributes/<uuid:pk>/edit/",
        rfattributes_views.RadioAttributesEditView.as_view(),
        name="radioattributes_edit",
    ),
    path(
        "radioattributes/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="radioattributes_changelog",
        kwargs={"model": models.RadioAttributes},
    ),
    # LocationAttributes URLs
    path(
        "locationattributes/", locationattributes.LocationAttributesListView.as_view(), name="locationattributes_list"
    ),
    # Order is important for these URLs to work (add/delete/edit) to be before any that require uuid/slug
    path(
        "locationattributes/add/",
        locationattributes.LocationAttributesCreateView.as_view(),
        name="locationattributes_add",
    ),
    path(
        "locationattributes/delete/",
        locationattributes.LocationAttributesBulkDeleteView.as_view(),
        name="locationattributes_bulk_delete",
    ),
    path(
        "locationattributes/edit/",
        locationattributes.LocationAttributesBulkEditView.as_view(),
        name="locationattributes_bulk_edit",
    ),
    path(
        "locationattributes/<uuid:pk>/",
        locationattributes.LocationAttributesView.as_view(),
        name="locationattributes",
    ),
    path(
        "locationattributes/<uuid:pk>/delete/",
        locationattributes.LocationAttributesDeleteView.as_view(),
        name="locationattributes_delete",
    ),
    path(
        "locationattributes/<uuid:pk>/edit/",
        locationattributes.LocationAttributesEditView.as_view(),
        name="locationattributes_edit",
    ),
    path(
        "locationattributes/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="locationattributes_changelog",
        kwargs={"model": models.LocationAttributes},
    ),
    # CircuitAttributes URLs
    path("circuitattributes/", circuitattributes.CircuitAttributesListView.as_view(), name="circuitattributes_list"),
    # Order is important for these URLs to work (add/delete/edit) to be before any that require uuid/slug
    path(
        "circuitattributes/add/", circuitattributes.CircuitAttributesCreateView.as_view(), name="circuitattributes_add"
    ),
    path(
        "circuitattributes/delete/",
        circuitattributes.CircuitAttributesBulkDeleteView.as_view(),
        name="circuitattributes_bulk_delete",
    ),
    path(
        "circuitattributes/edit/",
        circuitattributes.CircuitAttributesBulkEditView.as_view(),
        name="circuitattributes_bulk_edit",
    ),
    path("circuitattributes/<uuid:pk>/", circuitattributes.CircuitAttributesView.as_view(), name="circuitattributes"),
    path(
        "circuitattributes/<uuid:pk>/delete/",
        circuitattributes.CircuitAttributesDeleteView.as_view(),
        name="circuitattributes_delete",
    ),
    path(
        "circuitattributes/<uuid:pk>/edit/",
        circuitattributes.CircuitAttributesEditView.as_view(),
        name="circuitattributes_edit",
    ),
    path(
        "circuitattributes/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="circuitattributes_changelog",
        kwargs={"model": models.CircuitAttributes},
    ),
    path("circuitattributes/<uuid:pk>/rfds/", circuitattributes.CircuitRfds.as_view(), name="circuit_rfds"),
]

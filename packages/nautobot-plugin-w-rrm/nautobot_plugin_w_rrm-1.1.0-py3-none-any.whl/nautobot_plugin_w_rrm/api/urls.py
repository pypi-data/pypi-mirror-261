"""Django API urlpatterns declaration for w_rrm plugin."""

from rest_framework import routers

from nautobot_plugin_w_rrm.api import views

router = routers.DefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("radioattributes", views.RadioAttributesViewSet)
router.register("locationattributes", views.LocationAttributesViewSet)
router.register("circuitattributes", views.CircuitAttributesViewSet)


app_name = "nautobot_plugin_w_rrm-api"
urlpatterns = router.urls

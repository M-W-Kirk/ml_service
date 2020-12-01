
#---START----------------------------------------
# backend/server/apps/endpoints/urls.py file
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLAlgorithmStatusViewSet
from apps.endpoints.views import MLRequestViewSet

# Create the REST API router to the database models:
router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

# Create the URL pattern for accessing models:
# http://<server-ip>/api/ipar_v1/<object-name>
# PLEASE NOTE: "ipar_v1" is currently used for versioning control.
urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
]

#---END------------------------------------------
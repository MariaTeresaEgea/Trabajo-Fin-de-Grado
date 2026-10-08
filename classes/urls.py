from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    ClassViewSet,
    TeacherAvailabilityViewSet,
)


router = DefaultRouter()

router.register(
    "classes",
    ClassViewSet,
    basename="classes"
)

router.register(
    "availability",
    TeacherAvailabilityViewSet,
    basename="availability"
)


urlpatterns = [
    path("", include(router.urls)),
]
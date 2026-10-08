from django.urls import path

urlpatterns = []
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet, GuardianViewSet


router = DefaultRouter()

router.register(
    "students",
    StudentViewSet,
    basename="students"
)

router.register(
    "guardians",
    GuardianViewSet,
    basename="guardians"
)


urlpatterns = [
    path("", include(router.urls)),
]
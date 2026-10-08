from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    ProfileViewSet,
    TeacherViewSet,
    me,
)


router = DefaultRouter()

router.register(
    "users",
    UserViewSet,
    basename="users"
)

router.register(
    "profiles",
    ProfileViewSet,
    basename="profiles"
)

router.register(
    "teachers",
    TeacherViewSet,
    basename="teachers"
)


urlpatterns = [
    path("", include(router.urls)),
    path("me/", me, name="me"),
]
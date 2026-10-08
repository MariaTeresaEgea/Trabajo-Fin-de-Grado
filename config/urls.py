from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token"
    ),

    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),

    path(
        "api/",
        include("users.urls")
    ),

    path(
        "api/",
        include("students.urls")
    ),

    path(
        "api/",
        include("classes.urls")
    ),

    path(
        "api/",
        include("attendance.urls")
    ),
]
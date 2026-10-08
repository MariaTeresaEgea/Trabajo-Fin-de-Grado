from django.contrib import admin
from .models import Student, Guardian


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "level",
        "email",
        "active",
    )

    list_filter = (
        "active",
        "level",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
    )


@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "relationship",
        "phone",
    )

    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__username",
    )
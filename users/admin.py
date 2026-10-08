from django.contrib import admin
from .models import Profile, Teacher


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "phone")
    list_filter = ("role",)
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "specialty",
        "active",
    )

    list_filter = ("active",)

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "specialty",
    )
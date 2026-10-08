from django.contrib import admin
from .models import Class


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "subject",
        "teacher",
        "student",
        "date",
        "start_time",
        "end_time",
        "status",
        "modality",
    )

    list_filter = (
        "status",
        "modality",
        "date",
    )

    search_fields = (
        "title",
        "subject",
        "student__first_name",
        "student__last_name",
        "teacher__user__first_name",
        "teacher__user__last_name",
    )
    

from rest_framework import serializers

from .models import Attendance


class AttendanceSerializer(
    serializers.ModelSerializer
):

    student_name = serializers.SerializerMethodField()

    class_name = serializers.SerializerMethodField()

    status_display = serializers.CharField(
        source="get_status_display",
        read_only=True
    )

    class Meta:
        model = Attendance

        fields = (
            "id",
            "class_session",
            "class_name",
            "student",
            "student_name",
            "status",
            "status_display",
            "observations",
            "created_at",
        )

        read_only_fields = (
            "id",
            "class_name",
            "student_name",
            "status_display",
            "created_at",
        )

    def get_student_name(self, obj):
        return str(obj.student)

    def get_class_name(self, obj):
        return str(obj.class_session)
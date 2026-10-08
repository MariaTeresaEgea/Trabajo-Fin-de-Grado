from rest_framework import serializers

from .models import Class, TeacherAvailability


class ClassSerializer(serializers.ModelSerializer):

    teacher_name = serializers.SerializerMethodField()

    student_name = serializers.SerializerMethodField()

    modality_display = serializers.CharField(
        source="get_modality_display",
        read_only=True
    )

    status_display = serializers.CharField(
        source="get_status_display",
        read_only=True
    )

    recurrence_weekday_display = serializers.CharField(
        source="get_recurrence_weekday_display",
        read_only=True
    )

    class Meta:
        model = Class

        fields = (
            "id",
            "title",
            "subject",
            "teacher",
            "teacher_name",
            "student",
            "student_name",
            "date",
            "start_time",
            "end_time",
            "modality",
            "modality_display",
            "status",
            "status_display",
            "recurring",
            "recurrence_weekday",
            "recurrence_weekday_display",
            "recurrence_end",
            "observations",
            "created_at",
        )

        read_only_fields = (
            "id",
            "created_at",
            "teacher_name",
            "student_name",
            "modality_display",
            "status_display",
            "recurrence_weekday_display",
        )

    def get_teacher_name(self, obj):
        return (
            obj.teacher.user.get_full_name()
            or obj.teacher.user.username
        )

    def get_student_name(self, obj):
        return str(obj.student)


class TeacherAvailabilitySerializer(
    serializers.ModelSerializer
):

    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = TeacherAvailability

        fields = (
            "id",
            "teacher",
            "teacher_name",
            "weekday",
            "start_time",
            "end_time",
            "active",
        )

    def get_teacher_name(self, obj):
        return (
            obj.teacher.user.get_full_name()
            or obj.teacher.user.username
        )
    
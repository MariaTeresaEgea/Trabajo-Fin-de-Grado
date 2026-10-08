from rest_framework import viewsets

from .models import Attendance
from .serializers import AttendanceSerializer

from users.permissions import (
    IsAdminOrTeacherWrite,
    IsAuthenticatedReadOnly,
)


class AttendanceViewSet(viewsets.ModelViewSet):

    serializer_class = AttendanceSerializer

    def get_permissions(self):

        role = getattr(
            getattr(self.request.user, "profile", None),
            "role",
            None
        )

        if role in {"ADMIN", "TEACHER"}:
            return [IsAdminOrTeacherWrite()]

        return [IsAuthenticatedReadOnly()]

    def get_queryset(self):

        user = self.request.user

        queryset = Attendance.objects.select_related(
            "class_session",
            "student",
        )

        if user.is_superuser:
            return queryset.all()

        role = getattr(
            getattr(user, "profile", None),
            "role",
            None
        )

        if role == "ADMIN":
            return queryset.all()

        if role == "TEACHER":
            return queryset.filter(
                class_session__teacher__user=user
            )

        if role == "STUDENT":
            return queryset.filter(
                student__user=user
            )

        if role == "GUARDIAN":
            return queryset.filter(
                student__guardians__user=user
            ).distinct()

        return queryset.none()
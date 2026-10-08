from rest_framework import viewsets

from .models import Student, Guardian
from .serializers import (
    StudentSerializer,
    GuardianSerializer,
)

from users.permissions import (
    IsAdminOrTeacherWrite,
    IsAuthenticatedReadOnly,
)


class StudentViewSet(viewsets.ModelViewSet):

    serializer_class = StudentSerializer

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

        if user.is_superuser:
            return Student.objects.all()

        role = getattr(
            getattr(user, "profile", None),
            "role",
            None
        )

        if role == "ADMIN":
            return Student.objects.all()

        if role == "TEACHER":
            return Student.objects.filter(
                classes__teacher__user=user
            ).distinct()

        if role == "STUDENT":
            return Student.objects.filter(
                user=user
            )

        if role == "GUARDIAN":
            return Student.objects.filter(
                guardians__user=user
            ).distinct()

        return Student.objects.none()


class GuardianViewSet(viewsets.ModelViewSet):

    serializer_class = GuardianSerializer

    def get_permissions(self):

        role = getattr(
            getattr(self.request.user, "profile", None),
            "role",
            None
        )

        if role == "ADMIN":
            return [IsAdminOrTeacherWrite()]

        return [IsAuthenticatedReadOnly()]

    def get_queryset(self):

        user = self.request.user

        if user.is_superuser:
            return Guardian.objects.all()

        role = getattr(
            getattr(user, "profile", None),
            "role",
            None
        )

        if role == "ADMIN":
            return Guardian.objects.all()

        if role == "GUARDIAN":
            return Guardian.objects.filter(
                user=user
            )

        return Guardian.objects.none()
from rest_framework import viewsets

from .models import Class, TeacherAvailability
from .serializers import (
    ClassSerializer,
    TeacherAvailabilitySerializer,
)

from users.permissions import (
    IsAdminOrTeacherWrite,
    IsAuthenticatedReadOnly,
)


class ClassViewSet(viewsets.ModelViewSet):

    serializer_class = ClassSerializer

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
            return Class.objects.select_related(
                "teacher__user",
                "student"
            ).all()

        role = getattr(
            getattr(user, "profile", None),
            "role",
            None
        )

        queryset = Class.objects.select_related(
            "teacher__user",
            "student"
        )

        if role == "ADMIN":
            return queryset

        if role == "TEACHER":
            return queryset.filter(
                teacher__user=user
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

    def perform_create(self, serializer):

        if getattr(
            getattr(self.request.user, "profile", None),
            "role",
            None
        ) == "TEACHER":

            serializer.save(
                teacher=self.request.user.teacher
            )

        else:
            serializer.save()


class TeacherAvailabilityViewSet(
    viewsets.ModelViewSet
):

    serializer_class = TeacherAvailabilitySerializer

    def get_queryset(self):

        user = self.request.user

        if user.is_superuser:
            return TeacherAvailability.objects.all()

        role = getattr(
            getattr(user, "profile", None),
            "role",
            None
        )

        if role == "ADMIN":
            return TeacherAvailability.objects.all()

        if role == "TEACHER":
            return TeacherAvailability.objects.filter(
                teacher__user=user
            )

        return TeacherAvailability.objects.none()

    def get_permissions(self):

        return [IsAdminOrTeacherWrite()]
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        TEACHER = "TEACHER", "Profesor"
        STUDENT = "STUDENT", "Alumno"
        GUARDIAN = "GUARDIAN", "Familiar/Tutor"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_role_display()}"


class Teacher(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="teacher"
    )

    specialty = models.CharField(
        max_length=150,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username

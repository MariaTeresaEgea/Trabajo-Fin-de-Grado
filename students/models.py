from django.contrib.auth.models import User
from django.db import models


class Guardian(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="guardian"
    )

    relationship = models.CharField(
        max_length=50,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="student"
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)

    birth_date = models.DateField(
        null=True,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    level = models.CharField(
        max_length=100,
        blank=True
    )

    objectives = models.TextField(
        blank=True
    )

    observations = models.TextField(
        blank=True
    )

    guardians = models.ManyToManyField(
        Guardian,
        blank=True,
        related_name="students"
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
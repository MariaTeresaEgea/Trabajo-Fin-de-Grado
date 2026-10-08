from django.db import models

from students.models import Student
from users.models import Teacher


class Class(models.Model):

    class Modality(models.TextChoices):
        PRESENTIAL = "PRESENTIAL", "Presencial"
        ONLINE = "ONLINE", "Online"

    class Status(models.TextChoices):
        SCHEDULED = "SCHEDULED", "Programada"
        COMPLETED = "COMPLETED", "Realizada"
        CANCELLED = "CANCELLED", "Cancelada"
        RECOVERY = "RECOVERY", "Recuperación"

    class Weekday(models.IntegerChoices):
        MONDAY = 0, "Lunes"
        TUESDAY = 1, "Martes"
        WEDNESDAY = 2, "Miércoles"
        THURSDAY = 3, "Jueves"
        FRIDAY = 4, "Viernes"
        SATURDAY = 5, "Sábado"
        SUNDAY = 6, "Domingo"

    title = models.CharField(max_length=150)

    subject = models.CharField(max_length=100)

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="classes"
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="classes"
    )

    date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    modality = models.CharField(
        max_length=20,
        choices=Modality.choices,
        default=Modality.PRESENTIAL
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SCHEDULED
    )

    recurring = models.BooleanField(
        default=False
    )

    recurrence_weekday = models.IntegerField(
        choices=Weekday.choices,
        null=True,
        blank=True
    )

    recurrence_end = models.DateField(
        null=True,
        blank=True
    )

    observations = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.title} - {self.date}"


class TeacherAvailability(models.Model):

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="availability"
    )

    weekday = models.IntegerField(
        choices=Class.Weekday.choices
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = (
            "weekday",
            "start_time",
        )

    def __str__(self):
        return (
            f"{self.teacher} - "
            f"{self.get_weekday_display()} "
            f"{self.start_time}-{self.end_time}"
        )
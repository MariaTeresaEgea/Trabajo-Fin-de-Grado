from django.db import models
from classes.models import Class
from students.models import Student


class Attendance(models.Model):

    class Status(models.TextChoices):
        ATTENDED = "ATTENDED", "Asistió"
        JUSTIFIED = "JUSTIFIED", "Ausencia justificada"
        UNJUSTIFIED = "UNJUSTIFIED", "Ausencia no justificada"
        RECOVERED = "RECOVERED", "Recuperada"

    class_session = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="attendance_records"
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="attendance"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices
    )

    observations = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["class_session", "student"],
                name="unique_attendance_per_class_student",
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.class_session} - {self.status}"
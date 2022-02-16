from django.db import models


class Lecture(models.Model):
    name = models.CharField(max_length=32, null=False)
    students = models.ManyToManyField(
        to='students.Student',
        related_name='lectures',
        blank=True
    )

    class DifficultyLevel(models.IntegerChoices):
        LOW = 1, 'Low'
        NORMAL = 2, 'Normal'
        HIGH = 3, 'High'

    level = models.PositiveIntegerField(default=DifficultyLevel.LOW,
                                        choices=DifficultyLevel.choices)

from django.core.validators import MinValueValidator, MaxValueValidator, \
    RegexValidator
from django.db import models

# Create your models here.
from core_lms.validators import even_integer_validator


class Person(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    age = models.IntegerField(default=20, validators=[
        MinValueValidator(20),
        MaxValueValidator(120),
        even_integer_validator
    ])
    email = models.EmailField(max_length=64)
    phone_number = models.CharField(
        max_length=24,
        validators=[
            RegexValidator(
                r'^(\+\d\d?)?\(\d{3}\)(\d-?){7}$',
                message="Phone number should be in format +1(111)222-33-44"
            )
        ]
    )

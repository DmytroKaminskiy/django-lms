import datetime
import random

from django.db import models
from django.urls import reverse
from faker import Faker

# Create your models here.
from core_lms.models import Person


class Student(Person):
    enroll_date = models.DateField(default=datetime.datetime.today)
    graduate_date = models.DateField(default=datetime.datetime.today)
    inn = models.PositiveIntegerField(unique=True, null=True)
    group = models.ForeignKey(
        to='groups.Group',
        null=True,
        on_delete=models.SET_NULL,
        related_name='students'
    )

    @classmethod
    def generate_students(cls, count):
        faker = Faker()

        for _ in range(count):
            s = Student()
            s.first_name = faker.first_name()
            s.last_name = faker.last_name()
            s.age = random.randint(18, 80)

            s.save()

    def __str__(self):
        return f"Student({self.id}) {self.first_name} {self.last_name} " \
               f"{self.age} {self.phone_number} " \
               f"{self.enroll_date} {self.graduate_date}"

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def get_update_link(self):
        return reverse('students:update_students', kwargs={'id': self.id})

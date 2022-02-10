import datetime
import random

from django.db import models
# Create your models here.
from django.urls import reverse
from faker import Faker


class Group(models.Model):
    name = models.CharField(max_length=64, null=False)
    course = models.CharField(max_length=64, null=False)
    start_date = models.DateField(default=datetime.datetime.today)
    headman = models.OneToOneField(
        to='students.Student',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headed_group'
    )

    def __str__(self):
        return super().__str__() + f'({self.name} {self.course})'

    @classmethod
    def generate(cls, count):
        faker = Faker()
        for _ in range(count):
            group = Group()
            group.name = faker.job()
            group.course = str(random.randint(1, 10))
            group.start_date = (
                    datetime.datetime.today() -
                    datetime.timedelta(days=random.randint(1, 1000))
            )
            group.save()

    def get_absolute_url(self):
        return reverse('groups:group', kwargs={'id': self.id})

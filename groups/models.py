import datetime

from django.db import models


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=64, null=False)
    course = models.CharField(max_length=64, null=False)
    start_date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return super().__str__() + f'({self.name} {self.course})'

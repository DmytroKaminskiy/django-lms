# Generated by Django 3.2.11 on 2022-01-23 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='enroll_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 23, 9, 26, 3, 608608)),
        ),
        migrations.AddField(
            model_name='student',
            name='graduate_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default='', max_length=24),
            preserve_default=False,
        ),
    ]
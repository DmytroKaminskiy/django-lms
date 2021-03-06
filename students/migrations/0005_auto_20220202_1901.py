# Generated by Django 3.2.11 on 2022-02-02 19:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_alter_group_start_date'),
        ('students', '0004_auto_20220130_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='enroll_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]

# Generated by Django 3.2.11 on 2022-02-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='level',
            field=models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High')], default=1),
        ),
    ]

# Generated by Django 3.2.11 on 2022-02-06 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20220202_1901'),
        ('groups', '0002_alter_group_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='headman',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headed_group', to='students.student'),
        ),
    ]

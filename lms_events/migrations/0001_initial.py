# Generated by Django 3.2.11 on 2022-02-06 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0007_lecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EventHomeWorkComplete',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='lms_events.event')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.lecture')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.student')),
            ],
            bases=('lms_events.event',),
        ),
    ]

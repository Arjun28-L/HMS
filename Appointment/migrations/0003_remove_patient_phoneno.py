# Generated by Django 5.0.3 on 2024-05-14 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0002_remove_doctor_phoneno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='phoneno',
        ),
    ]

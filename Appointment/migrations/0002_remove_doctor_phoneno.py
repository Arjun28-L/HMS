# Generated by Django 5.0.3 on 2024-05-14 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='phoneno',
        ),
    ]

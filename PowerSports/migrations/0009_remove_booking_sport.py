# Generated by Django 5.0 on 2024-02-14 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PowerSports', '0008_alter_booking_sport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='sport',
        ),
    ]

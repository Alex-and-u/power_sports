# Generated by Django 5.0 on 2024-02-14 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PowerSports', '0007_booking_players_needed_booking_sport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PowerSports.sport'),
        ),
    ]

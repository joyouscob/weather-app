# Generated by Django 5.0.2 on 2024-02-24 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_remove_weatherhistory_location_day_constraint_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherhistory',
            old_name='weather_date',
            new_name='created_at',
        ),
    ]

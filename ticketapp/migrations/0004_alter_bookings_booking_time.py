# Generated by Django 4.0 on 2022-01-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0003_bookings_booking_time_bookings_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='booking_time',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 4.0 on 2022-02-01 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0007_remove_bookings_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payements',
            name='booking',
        ),
        migrations.DeleteModel(
            name='bookings',
        ),
        migrations.DeleteModel(
            name='payements',
        ),
    ]

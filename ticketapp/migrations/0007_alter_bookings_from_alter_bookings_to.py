# Generated by Django 4.0.2 on 2022-04-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0006_bookings_from_bookings_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='From',
            field=models.CharField(default='null', max_length=30),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='To',
            field=models.CharField(default='null', max_length=30),
        ),
    ]

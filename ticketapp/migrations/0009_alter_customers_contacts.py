# Generated by Django 4.0.2 on 2022-04-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0008_remove_customers_firstname_remove_customers_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='contacts',
            field=models.IntegerField(),
        ),
    ]

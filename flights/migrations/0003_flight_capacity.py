# Generated by Django 5.1.7 on 2025-03-31 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0002_alter_airport_city_passenger"),
    ]

    operations = [
        migrations.AddField(
            model_name="flight",
            name="capacity",
            field=models.IntegerField(default=50),
        ),
    ]

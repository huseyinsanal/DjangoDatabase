# Generated by Django 5.0.3 on 2024-04-01 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="musician",
            name="salary",
            field=models.IntegerField(
                default=0, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="musician",
            name="age",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(150),
                ]
            ),
        ),
    ]

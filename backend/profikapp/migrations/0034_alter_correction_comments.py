# Generated by Django 4.2.2 on 2023-08-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profikapp", "0033_remove_exercise_reasoning"),
    ]

    operations = [
        migrations.AlterField(
            model_name="correction",
            name="comments",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "minimum"), (1, "explicatif")], default=0
            ),
        ),
    ]

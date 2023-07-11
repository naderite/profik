# Generated by Django 4.2.2 on 2023-07-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profikapp", "0027_alter_question_exercise"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exercise",
            name="reasoning",
            field=models.PositiveBigIntegerField(
                choices=[(0, "normal"), (1, "récurrence"), (2, "absurd")]
            ),
        ),
    ]

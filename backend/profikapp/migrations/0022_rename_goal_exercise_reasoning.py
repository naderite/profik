# Generated by Django 4.2.2 on 2023-07-02 08:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("profikapp", "0021_rename_heading_exercise_head"),
    ]

    operations = [
        migrations.RenameField(
            model_name="exercise",
            old_name="goal",
            new_name="reasoning",
        ),
    ]

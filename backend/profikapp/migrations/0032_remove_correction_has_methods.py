# Generated by Django 4.2.2 on 2023-07-29 12:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("profikapp", "0031_remove_correction_has_theorem_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="correction",
            name="has_methods",
        ),
    ]
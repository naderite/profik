# Generated by Django 4.2.2 on 2023-07-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profikapp", "0030_course_resume"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="correction",
            name="has_theorem",
        ),
        migrations.AddField(
            model_name="correction",
            name="theorem_text",
            field=models.TextField(default="default_value_here"),
        ),
        migrations.AlterField(
            model_name="question",
            name="order",
            field=models.CharField(max_length=6),
        ),
    ]

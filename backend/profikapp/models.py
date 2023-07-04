from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=512)


class CoursePart(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, default=1, db_index=True
    )
    title = models.CharField(max_length=512)


class Exercise(models.Model):
    LENGTH_CHOICES = [
        (0, "court"),
        (1, "long"),
        (2, "probleme"),
    ]
    DIFFICULTY_CHOICES = [
        (0, "facile"),
        (1, "moyen"),
        (2, "difficile"),
    ]
    REASONING_CHOICES = [
        (0, "normal"),
        (1, "aléatoire"),
        (2, "récurrence"),
        (3, "absurd"),
    ]
    LEVEL_CHOICES = [
        ("bac tech", "Bac technique"),
        ("bac SC", "Bac science"),
        ("bac math", "Bac math"),
    ]
    level = models.CharField(max_length=512, default="bac", choices=LEVEL_CHOICES)
    course_part = models.ForeignKey(CoursePart, on_delete=models.CASCADE, default=1)
    length = models.PositiveSmallIntegerField(choices=LENGTH_CHOICES)
    reasoning = models.PositiveBigIntegerField(choices=REASONING_CHOICES)
    difficulty = models.PositiveSmallIntegerField(choices=DIFFICULTY_CHOICES, default=0)
    head = models.TextField(default="")


class Question(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, default=1)
    order = models.CharField(max_length=12)
    text = models.TextField()


class Correction(models.Model):
    COMMENT_CHOICES = [
        (0, "minimum"),
        (1, "moyen"),
        (2, "trés explicatif"),
    ]
    has_methods = models.BooleanField(default=False)
    comments = models.PositiveSmallIntegerField(choices=COMMENT_CHOICES, default=0)
    has_theorem = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    text = models.TextField(default="default_value_here")

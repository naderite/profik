from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=512)
    resume = models.CharField(max_length=10000, default="<p>$x=\frac{1}{y}$</p>")


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
        (1, "récurrence"),
        (2, "absurd"),
    ]
    LEVEL_CHOICES = [
        ("bac tech", "Bac technique"),
        ("bac SC", "Bac science"),
        ("bac math", "Bac math"),
    ]
    level = models.CharField(max_length=512, default="bac", choices=LEVEL_CHOICES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=10)
    course_part = models.ForeignKey(CoursePart, on_delete=models.CASCADE, default=1)
    length = models.PositiveSmallIntegerField(choices=LENGTH_CHOICES)
    reasoning = models.PositiveBigIntegerField(choices=REASONING_CHOICES)
    difficulty = models.PositiveSmallIntegerField(choices=DIFFICULTY_CHOICES, default=0)
    head = models.TextField(default="")


class Question(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, default=1)
    order = models.CharField(max_length=6)
    text = models.TextField()


class Correction(models.Model):
    COMMENT_CHOICES = [
        (0, "minimum"),
        (1, "moyen"),
        (2, "trés explicatif"),
    ]
    comments = models.PositiveSmallIntegerField(choices=COMMENT_CHOICES, default=0)
    theorem_text = models.TextField(default="default_value_here")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    text = models.TextField(default="default_value_here")

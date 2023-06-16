from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=512)


class CoursePart(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=512)


class Exercise(models.Model):
    LONGUEUR_CHOICES = [
        (0, 'court'),
        (1, 'long'),
        (2, 'probleme'),
    ]
    DIFFICULTE_CHOICES = [
        (0, 'facile'),
        (1, 'moyen'),
        (2, 'deficile'),
    ]
    niveau = models.CharField(max_length=512, default='bac')
    course_part_id = models.ForeignKey(CoursePart, on_delete=models.CASCADE,default=1)
    longueur = models.PositiveSmallIntegerField(choices=LONGUEUR_CHOICES)
    but = models.CharField(max_length=512)
    difficulte = models.PositiveSmallIntegerField(choices=DIFFICULTE_CHOICES, default=0)

class Question(models.Model):
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.CharField(max_length=12)
    text = models.TextField() 
class Correction(models.Model):
    COMMENTAIRES_CHOICES = [
        (0, 'minimum'),
        (1, 'moyen'),
        (2, 'trés explicatif'),
    ]
    nombre_de_methode = models.BooleanField(default=False)
    commentaires = models.PositiveSmallIntegerField(choices=COMMENTAIRES_CHOICES,default=0)
    theoreme = models.BooleanField(default=False)
    question_id = models.IntegerField(default=0)
    text = models.TextField(default='default_value_here')
    
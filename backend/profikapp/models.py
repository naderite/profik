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
    text = models.TextField(default='default_value_here')
    cours = models.ForeignKey(Course, on_delete=models.CASCADE)
    partie_cours = models.ForeignKey(CoursePart, on_delete=models.CASCADE)
    longueur = models.PositiveSmallIntegerField(choices=LONGUEUR_CHOICES)
    but = models.CharField(max_length=512)
    difficulte = models.PositiveSmallIntegerField(choices=DIFFICULTE_CHOICES, default=0)


class Correction(models.Model):
    COMMENTAIRES_CHOICES = [
        (0, 'minimum'),
        (1, 'moyen'),
        (2, 'trés explicatif'),
    ]
    
    ex_id = models.IntegerField()
    text = models.TextField(default='default_value_here')
    nombre_de_methode = models.BooleanField()
    commentaires = models.PositiveSmallIntegerField(choices=COMMENTAIRES_CHOICES)
    theoreme = models.BooleanField()

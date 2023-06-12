from django.db import models

class Exercice(models.Model):
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
    text = models.CharField(max_length=1024, default='default_value_here')
    cours = models.CharField(max_length=512)
    partie_cours = models.CharField(max_length=512)
    longueur = models.PositiveSmallIntegerField(choices=LONGUEUR_CHOICES)
    but = models.CharField(max_length=512)
    ex_id = models.IntegerField()
    difficulte = models.PositiveSmallIntegerField(choices=DIFFICULTE_CHOICES, default=0)


class Correction(models.Model):
    COMMENTAIRES_CHOICES = [
        (0, 'minimum'),
        (1, 'moyen'),
        (2, 'trés explicatif'),
    ]
    
    ex_id = models.IntegerField()
    text = models.CharField(max_length=1024, default='default_value_here')
    nombre_de_methode = models.BooleanField()
    commentaires = models.PositiveSmallIntegerField(choices=COMMENTAIRES_CHOICES)
    theoreme = models.BooleanField()
    cours = models.CharField(max_length=512, default="Cours1")

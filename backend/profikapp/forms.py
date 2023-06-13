from django import forms
from .models import Correction


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
COMMENTAIRES_CHOICES = [
    (0, 'minimum'),
    (1, 'moyen'),
    (2, 'trés explicatif'),
]

    
class ExerciseForm(forms.Form):
    exercise_niveau = forms.CharField(label='Exercise Niveau')
    exercise_cours = forms.CharField(label='Exercise Cours')
    exercise_partie_cours = forms.CharField(label='Exercise partie de cours')
    exercise_longueur = forms.ChoiceField(choices=LONGUEUR_CHOICES, label='Exercise longueur')
    exercise_but = forms.CharField(label='Exercise but')
    exercise_difficulte = forms.ChoiceField(choices=DIFFICULTE_CHOICES, label='Exercise difficulte')
    exercise_text = forms.CharField(label='Exercise text')

class CorrectionForm(forms.Form):
    text = forms.CharField(label='Correction Text')
    theoreme = forms.BooleanField(label='Theoreme')
    nombre_de_methode = forms.BooleanField(label='Nombre de Methode')
    commentaires = forms.IntegerField(label='Commentaires')
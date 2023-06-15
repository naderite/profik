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
THEOREME_CHOICES = [
        (True, 'inclus'),
        (False, 'non')
    ]
NOMBRE_DE_CHOICES = [(True, 'Seule'), (False, 'Multiple')] 


from django import forms
from .models import Course, CoursePart

class ExerciseForm(forms.Form):
    niveau = forms.CharField(label='Exercise Niveau')
    cours = forms.ModelChoiceField(queryset=Course.objects.all(), label='Exercise Cours')
    partie_cours = forms.ModelChoiceField(queryset=CoursePart.objects.all(), label='Exercise partie de cours')
    longueur = forms.ChoiceField(choices=LONGUEUR_CHOICES, label='Exercise longueur')
    but = forms.CharField(label='Exercise but')
    difficulte = forms.ChoiceField(choices=DIFFICULTE_CHOICES, label='Exercise difficulte')
    text = forms.CharField(widget=forms.Textarea(), label='Exercise text')


class CorrectionForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(), label='Exercise text')
    theoreme = forms.ChoiceField(
        choices=THEOREME_CHOICES,
        label='Theoreme',
        initial=True,
        widget=forms.HiddenInput(attrs={'value': True}),
    )
    nombre_de_methode = forms.ChoiceField(
        choices=NOMBRE_DE_CHOICES,
        initial=True,
        label='Nombre de Methode',
        widget=forms.HiddenInput(attrs={'value': True}),
    )    
    commentaires = forms.IntegerField(label='Commentaires', widget=forms.HiddenInput())

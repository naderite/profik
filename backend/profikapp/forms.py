from django import forms
from smart_selects.form_fields import ChainedModelChoiceField
from .models import Exercise, Course, CoursePart
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


class ExerciseForm(forms.Form):
    niveau = forms.CharField(label='Exercise Niveau')
    cours = forms.ModelChoiceField(queryset=Course.objects.all(), label='Exercise Cours')
    course_part_id = forms.ModelChoiceField(queryset=CoursePart.objects.all(), label='Exercise partie de cours')
    longueur = forms.ChoiceField(choices=LONGUEUR_CHOICES, label='Exercise longueur')
    but = forms.CharField(label='Exercise but')
    difficulte = forms.ChoiceField(choices=DIFFICULTE_CHOICES, label='Exercise difficulte')

class QuestionForm(forms.Form):
    order = forms.CharField(label="l'ordre de la question:")
    text = forms.CharField(widget=forms.Textarea,label='text')

class CorrectionForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea,label='text:')
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

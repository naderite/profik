from django import forms
from .models import Course, CoursePart


class ExerciseForm(forms.Form):
    """
    Form for creating an exercise.
    """
    LENGTH_CHOICES = [
    (0, 'court'),  # Short length
    (1, 'long'),  # Long length
    (2, 'probleme'),  # Problem length
    ]

    DIFFICULTY_CHOICES = [
        (0, 'facile'),  # Easy difficulty
        (1, 'moyen'),  # Medium difficulty
        (2, 'difficile'),  # Difficult difficulty
    ]
    level = forms.CharField(label='Niveau de l\'exercice')  # Exercise level
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label='Cours de l\'exercice')  # Exercise course
    course_part = forms.ModelChoiceField(queryset=CoursePart.objects.all(), label='Partie de cours de l\'exercice')  # Exercise course part
    length = forms.ChoiceField(choices=LENGTH_CHOICES, label='Longueur de l\'exercice')  # Exercise length
    goal = forms.CharField(label='But de l\'exercice')  # Exercise goal
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES, label='Difficulté de l\'exercice')  # Exercise difficulty


class QuestionForm(forms.Form):
    """
    Form for creating a question.
    """
    order = forms.CharField(label='Ordre de la question')  # Question order
    text = forms.CharField(widget=forms.Textarea, label='Texte de la question')  # Question text


class CorrectionForm(forms.Form):
    """
    Form for creating a correction.
    """
    COMMENT_CHOICES = [
    (0, 'minimum'),  # Minimum comments
    (1, 'moyen'),  # Medium comments
    (2, 'très explicatif'),  # Highly explanatory comments
    ]

    THEOREM_CHOICES = [
        (True, 'inclus'),  # Included theorem
        (False, 'non inclus'),  # Not included theorem
    ]

    METHODS_CHOICES = [
        (True, 'Unique'),  # Single number of methods
        (False, 'Multiple'),  # Multiple number of methods
    ]
    text = forms.CharField(widget=forms.Textarea, label='Texte de la correction')  # Correction text
    has_theorem = forms.ChoiceField(
        choices=THEOREM_CHOICES,
        label='Théorème',
        initial=True,
        widget=forms.HiddenInput,
    )  # Theorem inclusion
    has_methods = forms.ChoiceField(
        choices=METHODS_CHOICES,
        initial=True,
        label='Nombre de méthodes',
        widget=forms.HiddenInput,
    )  # Number of methods
    comments = forms.IntegerField(label='Commentaires', widget=forms.HiddenInput)  # Comment count

from django import forms
from .models import Course, CoursePart


class ExerciseForm(forms.Form):
    """
    Form for creating an exercise.
    """

    LEVEL_CHOICES = [
        ("bac tech", "Bac technique"),
        ("bac SC", "Bac science"),
        ("bac math", "Bac math"),
    ]
    LENGTH_CHOICES = [
        (0, "court"),  # Short length
        (1, "long"),  # Long length
        (2, "probleme"),  # Problem length
    ]

    DIFFICULTY_CHOICES = [
        (0, "facile"),  # Easy difficulty
        (1, "moyen"),  # Medium difficulty
        (2, "difficile"),  # Difficult difficulty
    ]

    head = forms.CharField(widget=forms.Textarea, label="Tête de l'exercice")
    level = forms.MultipleChoiceField(
        label="Niveau de l'exercice",
        choices=LEVEL_CHOICES,
        widget=forms.CheckboxSelectMultiple,  # Use CheckboxSelectMultiple widget for multi-choice
    )  # Exercise level
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), label="Cours de l'exercice"
    )  # Exercise course
    course_part = forms.ModelChoiceField(
        queryset=CoursePart.objects.all(), label="Partie de cours de l'exercice"
    )  # Exercise course part
    length = forms.ChoiceField(
        choices=LENGTH_CHOICES, label="Longueur de l'exercice"
    )  # Exercise length
    difficulty = forms.ChoiceField(
        choices=DIFFICULTY_CHOICES, label="Difficulté de l'exercice"
    )  # Exercise difficulty

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Modify the choices for the course field to use course titles
        course_choices = [(course.id, course.title) for course in Course.objects.all()]
        self.fields["course"].choices = course_choices

        # Similarly, modify the choices for the course_part field to use part titles
        course_part_choices = [
            (part.id, part.title) for part in CoursePart.objects.all()
        ]
        self.fields["course_part"].choices = course_part_choices


class QuestionForm(forms.Form):
    """
    Form for creating a question.
    """

    order = forms.CharField(label="Ordre de la question")  # Question order
    text = forms.CharField(
        widget=forms.Textarea, label="Texte de la question"
    )  # Question text


class CorrectionForm(forms.Form):
    """
    Form for creating a correction.
    """

    COMMENT_CHOICES = [
        (0, "minimum"),  # Minimum comments
        (1, "moyen"),  # Medium comments
        (2, "très explicatif"),  # Highly explanatory comments
    ]
    text = forms.CharField(
        widget=forms.Textarea, label="Texte de la correction"
    )  # Correction text
    theorem_text = forms.CharField(widget=forms.Textarea, label="Théoreme utilisé")
    comments = forms.IntegerField(
        label="Commentaires", widget=forms.HiddenInput
    )  # Comment count

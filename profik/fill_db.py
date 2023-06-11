import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profik.settings')
django.setup()

from profikapp.models import Exercice, Correction

# Create examples for Exercice
"""exercice_examples = []
for i in range(100):
    exercice = Exercice(
        cours='Mathematics',
        partie_de_cours='Algebra',
        longueur=i % 3,
        but='Solve equations',
        ex_id=i,
        text=f'This is the text for Exercice {i}',
        difficulte = i%3,
    )
    exercice_examples.append(exercice)

# Save the Exercice examples in a batch
Exercice.objects.bulk_create(exercice_examples)
"""
# Create examples for Correction
correction_examples = []
for i in range(1, 301):
    correction = Correction(
        ex_id=i//3,  # Not necessarily unique
        nombre_de_methode=i % 2 == 0,  # True if i is even, False if i is odd
        commentaires=i % 3,  # minimum, moyen, trés explicatif (repeating pattern)
        theoreme=i % 2 == 0,  # True if i is even, False if i is odd
        text=f'This is the text for Correction {i}'  # Add the text field value
    )
    correction_examples.append(correction)

# Save the Correction examples in a batch
Correction.objects.bulk_create(correction_examples)

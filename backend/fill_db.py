import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profik.settings')
django.setup()

from profikapp.models import Exercice, Correction

# Get the latest Exercice ID from the database
latest_exercice_id = Exercice.objects.last().ex_id if Exercice.objects.exists() else 0

# Create examples for Exercice
exercice_examples = []
for i in range(100):
    exercice = Exercice(
        cours='Mathematics',
        partie_de_cours='Algebra',
        longueur=i % 3,
        but='Solve equations',
        ex_id=latest_exercice_id + i + 1,  # Increment the ID by 1 for each new exercice
        text=f'This is the text for Exercice {i}',
        difficulte=i % 3,
    )
    exercice_examples.append(exercice)

# Save the Exercice examples in a batch
Exercice.objects.bulk_create(exercice_examples)

# Get the latest Correction ID from the database
latest_correction_id = Correction.objects.last().id if Correction.objects.exists() else 0

# Create examples for Correction
correction_examples = []
for i in range(1, 301):
    correction = Correction(
        ex_id=(latest_correction_id // 3) + 1,  # Not necessarily unique, incrementing by 1
        nombre_de_methode=i % 2 == 0,  # True if i is even, False if i is odd
        commentaires=i % 3,  # minimum, moyen, trés explicatif (repeating pattern)
        theoreme=i % 2 == 0,  # True if i is even, False if i is odd
        text=f'This is the text for Correction {i}'  # Add the text field value
    )
    correction_examples.append(correction)

# Save the Correction examples in a batch
Correction.objects.bulk_create(correction_examples)

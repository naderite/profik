from .models import Exercice, Correction
import random

def find_exercise(exercice_longueur, exercice_cours, exercice_partie_cours, exercice_but, exercice_difficulte):
    exercises = list(Exercice.objects.filter(
        longueur=exercice_longueur,
        cours=exercice_cours,
        partie_cours=exercice_partie_cours,
        but=exercice_but,
        difficulte=exercice_difficulte
    ))
    return random.choice(exercises) if exercises else None

def find_correction(correction_theoreme,correction_cours,correction_nombre_de_methode,correction_commentaire):
    corrections = list(Correction.objects.filter(theoreme = correction_theoreme,
                                            cours = correction_cours,
                                            nombre_de_methode = correction_nombre_de_methode,
                                            commentaires = correction_commentaire))
    return random.choice(corrections) if corrections else None
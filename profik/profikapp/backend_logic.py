from .models import Exercice, Correction

def find_exercise(exercice_longueur, exercice_cours, exercice_partie_cours, exercice_but, exercice_difficulte):
    exercises = Exercice.objects.filter(
        longueur=exercice_longueur,
        cours=exercice_cours,
        partie_de_cours=exercice_partie_cours,
        but=exercice_but,
        difficulte=exercice_difficulte
    )
    print(exercises)
    return exercises.first() if exercises.exists() else None

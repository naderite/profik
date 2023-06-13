from .models import Exercise, Correction
import random


def find_exercise(exercice_longueur, exercice_cours, exercice_partie_cours, exercice_but, exercice_difficulte):
    exercises = list(Exercise.objects.filter(
        longueur=exercice_longueur,
        cours=exercice_cours,
        partie_cours=exercice_partie_cours,
        but=exercice_but,
        difficulte=exercice_difficulte
    ))
    return random.choice(exercises) if exercises else None


def find_correction(correction_theoreme, correction_cours, correction_nombre_de_methode, correction_commentaire, ex_id):
    corrections = list(Correction.objects.filter(theoreme=correction_theoreme,
                                                cours=correction_cours,
                                                nombre_de_methode=correction_nombre_de_methode,
                                                commentaires=correction_commentaire,
                                                ex_id=ex_id))
    return random.choice(corrections) if corrections else None


def search_exercise(request):
    exercice_longueur = request.GET.get('longueur')
    exercice_cours = request.GET.get('cours')
    exercice_partie_cours = request.GET.get('partie_cours')
    exercice_but = request.GET.get('but')
    exercice_difficulte = request.GET.get('difficulte')
    return find_exercise(
        exercice_longueur,
        exercice_cours,
        exercice_partie_cours,
        exercice_but,
        exercice_difficulte,
    )


def search_correction(ex_id, request):
    correction_theoreme = bool(request.GET.get('theoreme'))
    correction_cours = request.GET.get('cours')
    correction_nombre_de_methode = bool(request.GET.get('nombre-de-methode'))
    correction_commentaire = request.GET.get('commentaire')
    return find_correction(
        correction_theoreme,
        correction_cours,
        correction_nombre_de_methode,
        correction_commentaire,
        ex_id,
    )

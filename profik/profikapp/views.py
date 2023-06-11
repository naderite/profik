from django.shortcuts import render
from .backend_logic import find_exercise, find_correction
# Create your views here.
def handler500(request):
    return render(request, '500.html', status=500)
    
def generateur_exercice(request):
    if request.method == 'GET':
        exercice_longueur = request.GET.get('longueur')
        exercice_cours = request.GET.get('cours')
        exercice_partie_cours = request.GET.get('partie_cours')
        exercice_but = request.GET.get('but')
        exercice_difficulte = request.GET.get('difficulte')
        exercise = find_exercise(
            exercice_longueur,
            exercice_cours,
            exercice_partie_cours,
            exercice_but,
            exercice_difficulte
        )

        correction_theoreme = bool(request.GET.get('theoreme'))
        correction_cours = request.GET.get('cours')
        correction_nombre_de_methode = bool(request.GET.get('nombre-de-methode'))
        correction_commentaire = request.GET.get('commentaire')
        correction = find_correction(
            correction_theoreme,
            correction_cours,
            correction_nombre_de_methode,
            correction_commentaire,
        )

        return render(request, 'profik/generateur.html', {'exercise': exercise, 'correction': correction})

    return render(request, 'profik/generateur.html', {'exercise': None, 'correction': None})


def show_exercise(request):
    exercice_longueur = request.GET.get('longueur')
    exercice_cours = request.GET.get('cours')
    exercice_partie_cours = request.GET.get('partie_cours')
    exercice_but = request.GET.get('but')
    exercice_difficulte = request.GET.get('difficulte')
    exercise = find_exercise(
        exercice_longueur,
        exercice_cours,
        exercice_partie_cours,
        exercice_but,
        exercice_difficulte
    )

    return render(request, 'profik/generateur.html', {'exercise': exercise})

def show_correction(request):
    correction_theoreme = bool(request.GET.get('theoreme')) #convert the string value to bool
    correction_cours = request.GET.get('cours')
    correction_nombre_de_methode = bool(request.GET.get('nombre-de-methode')) #convert the string value to bool
    correction_commentaire = request.GET.get('commentaire')
   
    correction = find_correction(
            correction_theoreme,
            correction_cours,
            correction_nombre_de_methode,
            correction_commentaire,
    )

    return render(request, 'profik/generateur.html', {'correction': correction})
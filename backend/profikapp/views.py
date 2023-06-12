from django.shortcuts import render
from .backend_logic import find_exercise, find_correction


# Create your views here.
def handler500(request):
    return render(request, '500.html', status=500)

def generateur_exercice(request):
    if request.method != 'GET':
        return render(request, 'profik/generateur.html', {'exercise': None})

    exercise = search_exercise(request)
    
    return render(request, 'profik/generateur.html', {'exercise': exercise})

def show_correction(request,exercise = None):
    if request.method != 'GET':
        return render(request, 'profik/correction.html', {'correction': None})
    ex_id = request.GET.get('ex_id')
    correction = search_correction(ex_id, request) if ex_id else None
    return render(request, 'profik/correction.html', {'correction': correction})

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

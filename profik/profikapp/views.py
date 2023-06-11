from django.shortcuts import render
from profikapp.models import Exercice, Correction
from .backend_logic import find_exercise
# Create your views here.
def handler500(request):
    return render(request, '500.html', status=500)
    
def generateur_exercice(request):
    if request.method == 'GET':
        return show_exercise(request)
    # Get the field names for Exercice and Correction models
    exercice_fields = [field.name for field in Exercice._meta.get_fields() if not field.name.startswith('_')]
    correction_fields = [field.name for field in Correction._meta.get_fields() if not field.name.startswith('_')]
  
    return render(request, 'profik/generateur.html', {'exercise': None})


def show_exercise(request):
    exercice_longueur = request.GET.get('longueur')
    exercice_cours = request.GET.get('cours')
    exercice_partie_cours = request.GET.get('partie_cours')
    exercice_but = request.GET.get('but')
    exercice_difficulte = request.GET.get('difficulte')
    print(exercice_longueur,
        exercice_cours,
        exercice_partie_cours,
        exercice_but,
        exercice_difficulte)
    exercise = find_exercise(
        exercice_longueur,
        exercice_cours,
        exercice_partie_cours,
        exercice_but,
        exercice_difficulte
    )

    return render(request, 'profik/generateur.html', {'exercise': exercise})
import itertools
from django.shortcuts import render, redirect
from .backend_logic import search_correction, search_exercise
from .forms import ExerciseForm, CorrectionForm
from .models import Exercise, Correction
from django.urls import reverse
from django import forms


# Create your views here.
def handler500(request):
    return render(request, '500.html', status=500)


def generateur_exercice(request):
    if request.method != 'GET':
        return render(request, 'profik/generateur.html', {'exercise': None})

    exercise = search_exercise(request)
    
    return render(request, 'profik/generateur.html', {'exercise': exercise})


def show_correction(request, exercise=None):
    if request.method != 'GET':
        return render(request, 'profik/correction.html', {'correction': None})
    ex_id = request.GET.get('ex_id')
    correction = search_correction(ex_id, request) if ex_id else None
    return render(request, 'profik/correction.html', {'correction': correction})


def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise_data = extract_exercise_data_from_form(form)
            exercise = Exercise()
            fill_exercise_data(exercise, exercise_data)
            exercise.save()
            # Redirect to the add correction page
            return redirect(reverse('add_correction', args=[exercise.id]))

    else:
        form = ExerciseForm()

    return render(request, 'profik/add_exercise.html', {'form': form})


def extract_exercise_data_from_form(form):
    exercise_niveau = form.cleaned_data['exercise_niveau']
    exercise_cours = form.cleaned_data['exercise_cours']
    exercise_partie_cours = form.cleaned_data['exercise_partie_cours']
    exercise_longueur = form.cleaned_data['exercise_longueur']
    exercise_but = form.cleaned_data['exercise_but']
    exercise_difficulte = form.cleaned_data['exercise_difficulte']
    exercise_text = form.cleaned_data['exercise_text']
    return (
        exercise_niveau,
        exercise_cours,
        exercise_partie_cours,
        exercise_longueur,
        exercise_but,
        exercise_difficulte,
        exercise_text,
    )


def fill_exercise_data(exercise, exercise_data):
    exercise.niveau = exercise_data[0]
    exercise.cours = exercise_data[1]
    exercise.partie_cours = exercise_data[2]
    exercise.longueur = exercise_data[3]
    exercise.but = exercise_data[4]
    exercise.difficulte = exercise_data[5]
    exercise.text = exercise_data[6]

def add_correction(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    theoreme_values = [True, False]
    nombre_de_methode_values = [True, False]
    commentaire_values = [0, 1, 2]
    combinations = list(itertools.product(theoreme_values, nombre_de_methode_values, commentaire_values))
    num_combinations = len(combinations)

    current_index = request.session.get('current_index', 0)

    if request.method == 'POST':
        form = CorrectionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            current_combination = combinations[current_index]

            correction = Correction(
                theoreme=current_combination[0],
                nombre_de_methode=current_combination[1],
                commentaires=current_combination[2],
                text=text,
                ex_id=exercise.id
            )
            correction.save()

            current_index += 1

            if current_index < num_combinations:
                next_combination = combinations[current_index]
                form = CorrectionForm(initial={
                    'text': '',
                    'theoreme': next_combination[0],
                    'nombre_de_methode': next_combination[1],
                    'commentaires': next_combination[2]
                })
                form.fields['theoreme'].widget = forms.HiddenInput()
                form.fields['nombre_de_methode'].widget = forms.HiddenInput()
                form.fields['commentaires'].widget = forms.HiddenInput()
    else:
        initial_combination = combinations[0]
        form = CorrectionForm(initial={
            'text': '',
            'theoreme': initial_combination[0],
            'nombre_de_methode': initial_combination[1],
            'commentaires': initial_combination[2]
        })
        form.fields['theoreme'].widget = forms.HiddenInput()
        form.fields['nombre_de_methode'].widget = forms.HiddenInput()
        form.fields['commentaires'].widget = forms.HiddenInput()

    request.session['current_index'] = current_index

    context = {
        'form': form,
        'exercise': exercise,
        'current_index': current_index,
        'num_combinations': num_combinations,
        'num_remaining_combinations': num_combinations - current_index - 1
    }
    return render(request, 'profik/add_correction.html', context)


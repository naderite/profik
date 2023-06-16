import itertools
from django.shortcuts import render, redirect
from .backend_logic import search_correction, search_exercise, fill_exercise_data,extract_exercise_data_from_form
from .forms import ExerciseForm, CorrectionForm, QuestionForm
from .models import Exercise, Correction, Question
from django.urls import reverse
from django.contrib import messages


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
            # Redirect to the add question page
            return redirect(reverse('add_question', args=[exercise.id]))

    else:
        form = ExerciseForm()

    return render(request, 'profik/add_exercise.html', {'form': form})

def add_questoin(request,exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            order = form.cleaned_data['order']
            text = form.cleaned_data['text']
            question = Question(order=order,text=text,exercise_id= exercise)
            question.save()
            # Redirect to the add correction page
            return redirect(reverse('add_correction', args=[question.id]))
    else:
        form= QuestionForm()
    return render(request, 'profik/add_question.html', {'form':form})

current_index = 0

def add_correction(request, question_id):
    global current_index
    question = Question.objects.get(id=question_id)
    theoreme_values = [True, False]
    nombre_de_methode_values = [True, False]
    commentaire_values = [0, 1, 2]
    combinations = list(itertools.product(theoreme_values, nombre_de_methode_values, commentaire_values))
    num_combinations = len(combinations)

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
                question_id=question.id
            )
            correction.save()

            current_index += 1

            if current_index >= num_combinations - 1:
                # Redirect to add_question view
                return redirect(reverse('add_question', args=[question.exercise_id.id]))
            next_combination = combinations[current_index]
            form = CorrectionForm(initial={
                'text': '',
                'theoreme': next_combination[0],
                'nombre_de_methode': next_combination[1],
                'commentaires': next_combination[2]
            })

    else:
        initial_combination = combinations[0]
        form = CorrectionForm(initial={
            'text': '',
            'theoreme': initial_combination[0],
            'nombre_de_methode': initial_combination[1],
            'commentaires': initial_combination[2]
        })

    context = {
        'form': form,
        'exercise': question,
        'current_index': current_index,
        'num_combinations': num_combinations,
        'num_remaining_combinations': num_combinations - current_index - 1,
        'form_errors': form.errors  # Include form errors in the context
    }
    return render(request, 'profik/add_correction.html', context)


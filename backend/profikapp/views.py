from django.shortcuts import render, redirect, get_object_or_404
from .backend_logic import (
    _search_correction,
    _search_exercise,
    _fill_exercise_data,
    _extract_exercise_data_from_form,
)
from .backend_logic import (
    _create_correction,
    _generate_combinations,
    _get_correction_context,
    _has_remaining_combinations,
    _get_correction_form,
)
from .forms import ExerciseForm, CorrectionForm, QuestionForm
from .models import Exercise, Question
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.


def handler500(request):
    """
    Handler for server error (500) response.
    """
    return render(request, "500.html", status=500)


def add_exercise(request):
    """
    Add a new exercise.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered add exercise page or a redirect to the add question page.
    """
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise_data = _extract_exercise_data_from_form(form)
            exercise = Exercise()
            _fill_exercise_data(exercise, exercise_data)
            exercise.save()
            # Redirect to the add question page
            return redirect(reverse("add_question", args=[exercise.id]))
    else:
        form = ExerciseForm()

    return render(request, "profik/add_exercise.html", {"form": form})


def add_question(request, exercise_id):
    """
    Add a new question to an exercise.

    Args:
        request (HttpRequest): The HTTP request object.
        exercise_id (int): The ID of the exercise.

    Returns:
        HttpResponse: The rendered add question page or a redirect to the add correction page.
    """
    exercise = Exercise.objects.get(id=exercise_id)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            order = form.cleaned_data["order"]
            text = form.cleaned_data["text"]
            question = Question(order=order, text=text, exercise=exercise)
            question.save()
            # Redirect to the add correction page
            return redirect(reverse("add_correction", args=[question.id]))
    else:
        form = QuestionForm()

    return render(request, "profik/add_question.html", {"form": form})


def add_correction(request, question_id):
    """
    Add a correction to a question.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question.

    Returns:
        HttpResponse: The rendered add correction page or a redirect to the add question page.
    """
    question = get_object_or_404(Question, id=question_id)
    combinations = _generate_combinations()
    # Retrieve current_index from session or generate new ones
    session = SessionStore(session_key=request.session.session_key)
    current_index = session.get("current_index")
    if not current_index:
        session["current_index"] = 0
        session.save()
    num_combinations = len(combinations)

    print(current_index, num_combinations)
    if request.method == "POST":
        form = CorrectionForm(request.POST)
        if form.is_valid():
            if not _has_remaining_combinations(current_index, num_combinations):
                # Update current_index in the session
                session["current_index"] = 0
                session.save()
                # Redirect to add_question view
                return redirect(reverse("add_question", args=[question.exercise.id]))

            text = form.cleaned_data["text"]
            current_combination = combinations[current_index]
            correction = _create_correction(question, current_combination, text)
            correction.save()
            current_index += 1

            session[
                "current_index"
            ] = current_index  # Update current_index in the session
            session.save()  # Save the session after updating the value
            next_combination = combinations[current_index]
            form = _get_correction_form(next_combination)
    else:
        initial_combination = combinations[0]
        form = _get_correction_form(initial_combination)

    context = _get_correction_context(question, num_combinations, combinations, form)
    return render(request, "profik/add_correction.html", context)

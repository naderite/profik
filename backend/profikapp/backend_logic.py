from .models import Exercise, Correction, Question
import random
import itertools
from .forms import CorrectionForm, ExerciseForm


def _find_exercise(exercise_length, exercise_course_part, exercise_goal, exercise_difficulty):
    """
    Finds an exercise based on the provided parameters.

    Returns a randomly selected exercise matching the parameters, or None if no exercise is found.
    """
    exercises = Exercise.objects.filter(
        length=exercise_length,
        course_part=exercise_course_part,
        goal=exercise_goal,
        difficulty=exercise_difficulty
    )
    return random.choice(exercises) if exercises else None


def _find_correction(correction_theorem, correction_course, correction_has_methods, correction_comments, question):
    """
    Finds a correction based on the provided parameters.

    Returns a randomly selected correction matching the parameters, or None if no correction is found.
    """
    corrections = Correction.objects.filter(
        has_theorem=correction_theorem,
        course=correction_course,
        has_methods=correction_has_methods,
        comments=correction_comments,
        question=question
    )
    return random.choice(corrections) if corrections else None


def _search_exercise(request):
    """
    Searches for an exercise based on the query parameters in the request.

    Returns a randomly selected exercise matching the query parameters, or None if no exercise is found.
    """
    exercise_form = ExerciseForm(request.GET or None)
    if exercise_form.is_valid():
        exercise_length = exercise_form.cleaned_data['length']
        exercise_course_part = exercise_form.cleaned_data['course_part']
        exercise_goal = exercise_form.cleaned_data['goal']
        exercise_difficulty = exercise_form.cleaned_data['difficulty']
        return _find_exercise(
            exercise_length,
            exercise_course_part,
            exercise_goal,
            exercise_difficulty,
        )
    return None


def _search_correction(question_id, request):
    """
    Searches for a correction based on the query parameters in the request.

    Returns a randomly selected correction matching the query parameters, or None if no correction is found.
    """
    correction_form = CorrectionForm(request.GET or None)
    if correction_form.is_valid():
        correction_theorem = correction_form.cleaned_data['theorem']
        correction_has_methods = correction_form.cleaned_data['has_methods']
        correction_comments = correction_form.cleaned_data['comments']
        question = Question.objects.get(id=question_id)
        return _find_correction(
            correction_theorem,
            correction_has_methods,
            correction_comments,
            question,
        )
    return None


def _extract_exercise_data_from_form(form):
    """
    Extracts exercise data from a form.

    Returns a tuple containing the extracted exercise data.
    """
    exercise_head = form.cleaned_data['head']
    exercise_level = form.cleaned_data['level']
    exercise_course_part = form.cleaned_data['course_part']
    exercise_length = form.cleaned_data['length']
    exercise_goal = form.cleaned_data['goal']
    exercise_difficulty = form.cleaned_data['difficulty']
    return exercise_level, exercise_course_part, exercise_length, exercise_goal, exercise_difficulty, exercise_head


def _fill_exercise_data(exercise, exercise_data):
    """
    Fills exercise data into the provided exercise instance.

    Modifies the exercise instance with the provided exercise data.
    """
    exercise.level = exercise_data[0]
    exercise.course_part = exercise_data[1]
    exercise.length = exercise_data[2]
    exercise.goal = exercise_data[3]
    exercise.difficulty = exercise_data[4]
    exercise.head = exercise_data[5]


def _generate_combinations():
    theorem_values = [True, False]
    number_of_methods_values = [True, False]
    comment_values = [0, 1, 2]
    return list(itertools.product(theorem_values, number_of_methods_values, comment_values))


def _create_correction(question, combination, text):
    return Correction.objects.create(
        has_theorem=combination[0],
        has_methods=combination[1],
        comments=combination[2],
        text=text,
        question=question
    )


def _has_remaining_combinations(current_index,num_combinations):
    return current_index < num_combinations - 1


def _get_correction_form(combination):
    return CorrectionForm(initial={
        'text': '',
        'has_theorem': combination[0],
        'has_methods': combination[1],
        'comments': combination[2]
    })


def _get_correction_context(question, num_combinations, combinations, form):
    return {
        'form': form,
        'question': question,
        'current_index': num_combinations - len(combinations),
        'num_combinations': num_combinations,
        'num_remaining_combinations': len(combinations),
        'form_errors': form.errors  # Include form errors in the context
    }

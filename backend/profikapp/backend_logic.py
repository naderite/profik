from .models import Exercise, Correction,Question
import random

def find_exercise(exercise_length, exercise_course_part, exercise_goal, exercise_difficulty):
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


def find_correction(correction_theorem, correction_course, correction_has_methods, correction_comments, question):
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



def search_exercise(request):
    """
    Searches for an exercise based on the query parameters in the request.

    Returns a randomly selected exercise matching the query parameters, or None if no exercise is found.
    """
    exercise_length = request.GET.get('length')
    exercise_course_part = request.GET.get('course_part')
    exercise_goal = request.GET.get('goal')
    exercise_difficulty = request.GET.get('difficulty')
    return find_exercise(
        exercise_length,
        exercise_course_part,
        exercise_goal,
        exercise_difficulty,
    )


def search_correction(question_id, request):
    """
    Searches for a correction based on the query parameters in the request.

    Returns a randomly selected correction matching the query parameters, or None if no correction is found.
    """
    correction_theorem = bool(request.GET.get('theorem'))
    correction_course = request.GET.get('course')
    correction_has_methods = bool(request.GET.get('has_methods'))
    correction_comments = request.GET.get('comments')
    question = Question.objects.get(id=question_id)
    return find_correction(
        correction_theorem,
        correction_course,
        correction_has_methods,
        correction_comments,
        question,
    )


def extract_exercise_data_from_form(form):
    """
    Extracts exercise data from a form.

    Returns a tuple containing the extracted exercise data.
    """
    exercise_level = form.cleaned_data['level']
    exercise_course_part = form.cleaned_data['course_part']
    exercise_length = form.cleaned_data['length']
    exercise_goal = form.cleaned_data['goal']
    exercise_difficulty = form.cleaned_data['difficulty']
    return exercise_level, exercise_course_part, exercise_length, exercise_goal, exercise_difficulty


def fill_exercise_data(exercise, exercise_data):
    """
    Fills exercise data into the provided exercise instance.

    Modifies the exercise instance with the provided exercise data.
    """
    exercise.level = exercise_data[0]
    exercise.course_part = exercise_data[1]
    exercise.length = exercise_data[2]
    exercise.goal = exercise_data[3]
    exercise.difficulty = exercise_data[4]

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profik.settings')
django.setup()
import itertools

from profikapp.models import Course, CoursePart, Exercise, Question, Correction

# Define the choices for Exercise fields
LENGTH_CHOICES = [
    0, 1, 2,
]
DIFFICULTY_CHOICES = [
    0, 1, 2,
]
LEVEL_CHOICES = [
    'bac math',
    'bac tech',
]

COMMENT_CHOICES = [
    0, 1, 2,
]

# Create courses and course parts
course = Course.objects.create(course_title='limite et continuite')
course_part = CoursePart.objects.create(course=course, part_title='limite')
course_part = CoursePart.objects.create(course=course, part_title='continuite')

# Generate all combinations of choices
exercise_combinations = list(itertools.product(LENGTH_CHOICES, DIFFICULTY_CHOICES, LEVEL_CHOICES))
correction_combinations = list(itertools.product([True, False], COMMENT_CHOICES, [True, False]))

# Create exercises, questions, and corrections for each combination
for exercise_combination in exercise_combinations:
    length, difficulty, level = exercise_combination

    # Create exercise
    exercise = Exercise.objects.create(
        length=length,
        difficulty=difficulty,
        level=level,
        course_part=course_part,
        goal=f"Goal for {length}-{difficulty}-{level}",
        heading=f"Heading for {length}-{difficulty}-{level}"
    )

    # Create questions for exercise
    for i in range(3):  # Create 3 questions for each exercise
        question = Question.objects.create(
            exercise=exercise,
            order=str(i),
            text=f"Question {i} for exercise {exercise.id}"
        )

        # Create corrections for question
        for correction_combination in correction_combinations:
            has_theorem, comments, has_methods = correction_combination
            correction = Correction.objects.create(
                has_methods=has_methods,
                comments=comments,
                has_theorem=has_theorem,
                question=question,
                text=f"Correction for question {question.id}, has_theorem={has_theorem}, comments={comments}, has_methods={has_methods}"
            )

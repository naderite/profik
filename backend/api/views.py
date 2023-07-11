import random

from django.http import JsonResponse
from django.views import View

from profikapp.models import Course, CoursePart, Exercise, Correction, Question

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    CoursePartSerializer,
    ExerciseSerializer,
    CorrectionSerializer,
    QuestionSerializer,
)


class CourseAPIView(View):
    def get(self, request):
        courses = Course.objects.all().values("id", "title")
        return JsonResponse({"courses": list(courses)})


class CoursePartAPIView(APIView):
    def get(self, request):
        course_parts = CoursePart.objects.all()
        serializer = CoursePartSerializer(course_parts, many=True)
        return Response(serializer.data)


class SearchExercise(View):
    def get(self, request):
        if request.method != "GET":
            return JsonResponse({"error": "Invalid request method"})

        # Extract the form data from the GET request
        course_part = request.GET.get("coursePart")
        length = request.GET.get("length")
        reasoning = request.GET.get("reasoning")
        difficulty = request.GET.get("difficulty")
        has_methods = request.GET.get("hasMethods") == "true"
        has_theorem = request.GET.get("hasTheorem") == "true"
        comments = request.GET.get("comments")

        # Filter the exercises based on the provided filters
        # if the reasoning is set to random don't include in the filter
        if reasoning == "3":
            exercises = Exercise.objects.filter(
                course_part=course_part,
                length=length,
                difficulty=difficulty,
            )
            print(exercises)

        else:
            exercises = Exercise.objects.filter(
                course_part=course_part,
                length=length,
                reasoning=reasoning,
                difficulty=difficulty,
            )
        if exercises.exists():
            # Get a random exercise from the filtered exercises
            exercise = random.choice(exercises)
            exercise_data = self.extract_exercise_data(
                exercise, has_methods, has_theorem, comments
            )
            # Return the exercise data as JSON response
            return JsonResponse({"exercise": exercise_data})
        else:
            # Handle the case when no exercises are found
            return JsonResponse({"error": "No exercises found"})

    def extract_exercise_data(self, exercise, has_methods, has_theorem, comments):
        questions = exercise.question_set.all()
        exercise_data = {
            "exercise": ExerciseSerializer(exercise).data,
            "questions": [],
        }

        for question in questions:
            if correction := Correction.objects.filter(
                question=question,
                has_methods=has_methods,
                has_theorem=has_theorem,
                comments=comments,
            ).first():
                correction_data = CorrectionSerializer(correction).data
            else:
                correction_data = None

            question_data = QuestionSerializer(question).data
            question_data["correction"] = correction_data
            exercise_data["questions"].append(question_data)

        return exercise_data

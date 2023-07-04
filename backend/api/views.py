import random

# Create your views here.
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
        has_methods = request.GET.get("hasMethods")
        has_theorem = request.GET.get("hasTheorem")
        comments = request.GET.get("comments")

        # Filter the exercises based on the provided filters
        exercises = Exercise.objects.filter(
            course_part=course_part,
            length=length,
            reasoning=reasoning,
            difficulty=difficulty,
        )
        if exercises.exists():
            # Get a random exercise from the filtered exercises
            exercise = random.choice(exercises)
            # Retrieve the questions and correction for each exercise
            exercise_data = []
            questions = exercise.question_set.all()
            for question in questions:
                correction = question.correction_set.filter(
                    has_methods=has_methods,
                    has_theorem=has_theorem,
                    comments=comments,
                )

                exercise_data.append(
                    {
                        "exercise": ExerciseSerializer(exercise).data,
                        "questions": QuestionSerializer(questions, many=True).data,
                        "corrections": CorrectionSerializer(correction, many=True).data,
                    }
                )

            # Return the exercise data as JSON response
            return JsonResponse({"exercise": exercise_data})
        else:
            # Handle the case when no exercises are found
            return JsonResponse({"error": "No exercises found"})

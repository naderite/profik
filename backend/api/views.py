import random
import logging
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
    CourseSerializer,
)

logger = logging.getLogger("main")


class CourseAPIView(View):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse({"courses": serializer.data})


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
        level = request.GET.get("level")
        course_part = request.GET.get("coursePart")
        length = request.GET.get("length")
        difficulty = request.GET.get("difficulty")
        has_theorem = request.GET.get("hasTheorem") == "true"
        comments = request.GET.get("comments")

        # logging message
        logging_message = f"level: {level}; course part: {course_part}; length: {length}; difficulty: {difficulty}; has theorem: {has_theorem}; comments: {comments}"
        logger.info(logging_message)
        # Filter the exercises based on the provided filters

        exercises = Exercise.objects.filter(
            level__contains=level,
            course_part=course_part,
            length=length,
            difficulty=difficulty,
        )
        if exercises.exists():
            # Get a random exercise from the filtered exercises
            exercise = random.choice(exercises)
            exercise_data = self.extract_exercise_data(exercise, has_theorem, comments)
            # Return the exercise data as JSON response
            return JsonResponse({"exercise": exercise_data})
        else:
            # Handle the case when no exercises are found
            return JsonResponse({"error": "No exercises found"})

    def extract_exercise_data(self, exercise, has_theorem, comments):
        questions = exercise.question_set.all()
        exercise_data = {
            "exercise": ExerciseSerializer(exercise).data,
            "questions": [],
        }

        for question in questions:
            if correction := Correction.objects.filter(
                question=question,
                comments=comments,
            ).first():
                correction_data = CorrectionSerializer(correction).data
                if not has_theorem:
                    correction_data["theorem_text"] = ""
            else:
                correction_data = None

            question_data = QuestionSerializer(question).data
            question_data["correction"] = correction_data
            exercise_data["questions"].append(question_data)

        return exercise_data


class ExerciseAPIView(APIView):
    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)

    def post(self, request):
        course_id = request.data.get("course_id")
        exercises = Exercise.objects.filter(course_id=course_id)
        if exercises.exists():
            exercises_list = []
            for exercise in exercises:
                # Get a random exercise from the filtered exercises
                exercise_data = self.extract_exercise_data(exercise)
                # Return the exercise data as JSON response
                exercises_list.append(exercise_data)
                # log exercises
                logging_message = (
                    f"exercise id: {exercise.id};\n exercise data: {exercise_data}"
                )
                logger.info(logging_message)
            return JsonResponse({"exercises": exercises_list})

        else:
            # Handle the case when no exercises are found
            return JsonResponse({"error": "No exercises found"})

    def extract_exercise_data(self, exercise):
        questions = exercise.question_set.all()
        exercise_data = {
            "exercise": ExerciseSerializer(exercise).data,
            "questions": [],
        }

        for question in questions:
            if correction := Correction.objects.filter(
                question=question,
                comments=1,
            ).first():
                correction_data = CorrectionSerializer(correction).data
                logging_message = f"correction id: {correction.id};\n correction data: {correction_data}"
                logger.info(logging_message)
            else:
                correction_data = None

            question_data = QuestionSerializer(question).data
            logging_message = (
                f"question id: {question.id};\n question data: {question_data}"
            )
            logger.info(logging_message)
            question_data["correction"] = correction_data
            exercise_data["questions"].append(question_data)

        return exercise_data

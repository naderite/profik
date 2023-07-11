from rest_framework import serializers
from profikapp.models import CoursePart, Question, Correction, Exercise


class CoursePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePart
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["order", "text"]


class CorrectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correction
        fields = ["has_methods", "comments", "has_theorem", "text"]


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            "level",
            "course_part",
            "length",
            "reasoning",
            "difficulty",
            "head",
        ]

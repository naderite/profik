from rest_framework import serializers
from profikapp.models import Course, CoursePart


class CoursePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePart
        fields = "__all__"

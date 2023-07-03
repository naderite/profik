from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
from profikapp.models import Course, CoursePart
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CoursePartSerializer


class CourseAPIView(View):
    def get(self, request):
        courses = Course.objects.all().values("id", "title")
        return JsonResponse({"courses": list(courses)})


class CoursePartAPIView(APIView):
    def get(self, request):
        course_parts = CoursePart.objects.all()
        serializer = CoursePartSerializer(course_parts, many=True)
        return Response(serializer.data)

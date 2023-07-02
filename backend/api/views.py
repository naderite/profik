from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
from profikapp.models import Course, CoursePart


class CourseAPIView(View):
    def get(self, request):
        courses = Course.objects.all().values("id", "course_title")
        return JsonResponse({"courses": list(courses)})


class CoursePartAPIView(View):
    def get(self, request):
        course_id = request.GET.get("course_id")
        course_parts = CoursePart.objects.filter(course_id=course_id).values(
            "id", "part_title"
        )
        return JsonResponse({"course_parts": list(course_parts)})

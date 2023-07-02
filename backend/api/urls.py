from django.urls import path
from .views import CourseAPIView, CoursePartAPIView

urlpatterns = [
    path("api/courses/", CourseAPIView.as_view(), name="course-api"),
    path("api/course-parts/", CoursePartAPIView.as_view(), name="course-part-api"),
]

from django.urls import path
from .views import CourseAPIView, CoursePartAPIView, SearchExercise

urlpatterns = [
    path("api/courses/", CourseAPIView.as_view(), name="course-api"),
    path("api/course-parts/", CoursePartAPIView.as_view(), name="course-part-api"),
    path("api/submit/", SearchExercise.as_view(), name="submit-form"),
]

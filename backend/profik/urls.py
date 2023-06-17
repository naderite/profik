from django.contrib import admin
from django.urls import path, include
from django.views.defaults import server_error as handler500
from profikapp.views import exercise_generator, handler500 as custom_handler500, show_correction, add_exercise, add_correction,add_question





urlpatterns = [
    path("admin/", admin.site.urls),
    path("generateur/", exercise_generator, name="exercise_generator"),
    path("correction/<int:exercise>/", show_correction, name="show_correction"),
    path('exercise/add/', add_exercise, name='add_exercise'),
    path('correction/add/<int:question_id>/', add_correction, name='add_correction'),
    path('question/add/<int:exercise_id>/', add_question, name='add_question'),
   
]


handler500 = custom_handler500  # Assign the custom handler500 view function to handler500


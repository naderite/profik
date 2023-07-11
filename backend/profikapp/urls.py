from .views import handler500 as custom_handler500, add_exercise, add_correction,add_question
from django.urls import path
from django.views.defaults import server_error as handler500



handler500 = custom_handler500  # Assign the custom handler500 view function to handler500

urlpatterns = [
    path('exercise/add/', add_exercise, name='add_exercise'),
    path('correction/add/<int:question_id>/', add_correction, name='add_correction'),
    path('question/add/<int:exercise_id>/', add_question, name='add_question'),
   
]






from django.contrib import admin
from django.urls import path
from django.views.defaults import server_error as handler500
from profikapp.views import generateur_exercice, handler500 as custom_handler500, show_correction, add_exercise, add_correction



urlpatterns = [
    path("admin/", admin.site.urls),
    path("generateur/", generateur_exercice, name="generateur_exercice"),
    path("correction/<int:exercise>/", show_correction, name="show_correction"),
    path('exercise/add/', add_exercise, name='add_exercise'),
    path('correction/add/<int:exercise_id>/', add_correction, name='add_correction'),
]


handler500 = custom_handler500  # Assign the custom handler500 view function to handler500


"""
URL configuration for profik project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.defaults import server_error as handler500
from profikapp.views import generateur_exercice, handler500 as custom_handler500, show_correction


urlpatterns = [
    path("admin/", admin.site.urls),
    path("generateur/", generateur_exercice, name="generateur_exercice"),
    path("correction/<int:exercise>/", show_correction, name="show_correction"),
]


handler500 = custom_handler500  # Assign the custom handler500 view function to handler500


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("profikapp.urls")),
    path("", include("api.urls")),
]

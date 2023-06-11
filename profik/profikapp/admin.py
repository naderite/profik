from django.contrib import admin

# Register your models here.
from .models import Exercice
from .models import Correction

admin.site.register(Exercice)
admin.site.register(Correction)
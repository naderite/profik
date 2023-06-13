from django.contrib import admin

# Register your models here.
from .models import Exercise
from .models import Correction

admin.site.register(Exercise)
admin.site.register(Correction)
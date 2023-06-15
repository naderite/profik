from django.contrib import admin

# Register your models here.
from .models import Exercise, Correction, Course, CoursePart


admin.site.register(Exercise)
admin.site.register(Correction)
admin.site.register(Course)
admin.site.register(CoursePart)
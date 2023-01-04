from django.contrib import admin

# Register your models here.
from .models import Subject, SubjectCombination
admin.site.register(SubjectCombination)
admin.site.register(Subject)
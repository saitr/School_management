from django.contrib import admin
from .models import DeclareResult
from .models import StudentMarks
# Register your models here.
# admin.site.register(DeclareResult)
# admin.site.register(StudentMarks)


class StudentMarksInline(admin.TabularInline):
    model = StudentMarks
    extra = 0


class MarksAdmin(admin.ModelAdmin):
    inlines = [StudentMarksInline]
    class Meta:
        model = DeclareResult



admin.site.register(DeclareResult,MarksAdmin)
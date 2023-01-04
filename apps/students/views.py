from django.shortcuts import render
from .models import Student
from rest_framework import generics
from .serializers import StudentAddSerializer, StudentListSerializer
# Create your views here.
class StudentsAdd(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentAddSerializer


class StudentsList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
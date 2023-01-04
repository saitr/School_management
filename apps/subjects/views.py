from django.shortcuts import render
from rest_framework import generics
from .models import Subject
from .serializers import SubjectSerializer
# Create your views here.

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
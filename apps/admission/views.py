from django.shortcuts import render
from rest_framework import generics
from .models import Admission_form
from .serializers import AdmissionFormSerializer, AdmissionListSerializer
from apps.users.mixins import CustomLoginRequiredMixin

# Create your views here.


class AdmissionFormView(generics.CreateAPIView):
    queryset = Admission_form.objects.all()
    serializer_class = AdmissionFormSerializer


class AdmissionListView(CustomLoginRequiredMixin,generics.ListAPIView):
    queryset = Admission_form.objects.all()
    serializer_class = AdmissionListSerializer
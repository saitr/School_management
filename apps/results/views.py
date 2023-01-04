from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
import json
from .models import DeclareResult
from .serializers import resultAddSerializer, ResultListSerializer

# Create your views here.


class addResult(generics.ListCreateAPIView):
    queryset = DeclareResult.objects.all()
    serializer_class = resultAddSerializer


class ResultList(generics.ListAPIView):
    queryset = DeclareResult.objects.all()
    serializer_class = ResultListSerializer
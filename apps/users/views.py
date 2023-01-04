from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSignInSerializer

# Create your views here.


class UserSignIn(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignInSerializer
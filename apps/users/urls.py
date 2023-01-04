from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.UserSignIn.as_view(), name='user_sign_in'),
   
]

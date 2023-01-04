from django.urls import path
from . import views

urlpatterns = [
    path('',views.SubjectView.as_view(),name='subject'),\
]
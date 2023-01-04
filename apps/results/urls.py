from django.urls import path, re_path
from . import views

app_name = 'results'

urlpatterns = [
    path('add/', views.addResult.as_view(), name='declare_result'),
    path('list/', views.ResultList.as_view(), name='result_list'),
]

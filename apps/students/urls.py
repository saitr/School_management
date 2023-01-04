from django.urls import path
from .views import StudentsAdd, StudentsList
urlpatterns = [
    path('add', StudentsAdd.as_view(), name = 'students add'),
    path('list', StudentsList.as_view(), name = 'students list'),

]
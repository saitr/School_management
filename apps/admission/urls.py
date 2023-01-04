from django.urls import path
from .views import AdmissionFormView, AdmissionListView

urlpatterns = [
    path('response/',AdmissionFormView.as_view(), name = 'admission-response' ),
    path('list/', AdmissionListView.as_view(), name = 'admission-list')
]
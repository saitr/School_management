from rest_framework import serializers
from .models import StudentClass


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ('class_name', 'section')
        

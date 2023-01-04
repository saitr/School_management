from rest_framework import serializers
from .models import Student


class StudentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'




class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['firstname','student_roll']
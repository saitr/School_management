from rest_framework import serializers
from .models import DeclareResult
from apps.students.serializers import StudentNameSerializer
# from apps.students.models import Student
# from apps.subjects.models import SubjectCombination
from apps.subjects.serializers import SubjectSerializer

class resultAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeclareResult
        fields = '__all__'


# class ResultSubSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubjectCombination
#         fields = ['results']

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeclareResult
        fields = ['marks']

class ResultListSerializer(serializers.ModelSerializer):
    student_name = StudentNameSerializer(many=True,source='results_details')
    student_results = SubjectSerializer(many=True,source='result_subjects')
    class Meta:
        model = DeclareResult
        fields = ['student_name','student_results',]


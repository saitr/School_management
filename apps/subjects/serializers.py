from rest_framework import serializers
from .models import Subject
# from apps.results.serializers import MarksSerializer
from apps.results.models import DeclareResult

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeclareResult
        fields = ('marks')
# class SubjectSerializer(serializers.ModelSerializer):
#     # marks = MarksSerializer(read_only=True,source='results_marks',many=True)
#     class Meta:
#         model = Subject
#         fields = ('subject_name','subject_code','results')
        # depth=1
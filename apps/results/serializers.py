from rest_framework import serializers
from .models import DeclareResult
# from apps.students.serializers import StudentNameSerializer
from apps.students.models import Student
from apps.subjects.models import Subject
# from .models import StudentMarks
# from apps.subjects.models import SubjectCombination
# from apps.subjects.serializers import SubjectSerializer
from apps.student_classes.serializers import StudentClassSerializer
from apps.student_classes.models import StudentClass
from .models import StudentMarks
class resultAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeclareResult
        fields = '__all__'


# class ResultSubSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubjectCombination
#         fields = ['results']
class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('firstname','lastname','student_roll')


class SubjectSerializer(serializers.ModelSerializer):
    # marks = MarksSerializer(read_only=True,source='results_marks',many=True)
    class Meta:
        model = Subject
        fields = ('subject_name',)

# class MarksSerializer(serializers.ModelSerializer):
#     # subject_details = SubjectSerializer()
#     class Meta:
#         model = StudentMarks
#         fields = ('subject','marks')
class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ('class_name', 'section')
        

class StudentMarksSerializer(serializers.ModelSerializer):
    student_subjects = SubjectSerializer(read_only=True)
    class Meta:
        model = StudentMarks
        fields = ('student_subjects','marks')


class ResultListSerializer(serializers.ModelSerializer):
    # student_name = StudentNameSerializer(many=True)
    student_details = StudentNameSerializer(read_only=True)
    student_marks = StudentMarksSerializer(read_only=True)
    student_class = StudentClassSerializer(read_only=True)
    # student_results = SubjectSerializer()
    # student_class = StudentClassSerializer(read_only=True)
    # marks = MarksSerializer()
    class Meta:
        model = DeclareResult
        fields = ['student_details','student_class','student_marks']
        # fields = ('student_details','student_class','student_marks')
        # depth=1
        # fields =('select_class',"select_student","student_marks")
  
    # def create(self,validated_data):
    #     DeclareResult.objects.create(
    #         validated_data.student_name  = student_name
    #     )   


    

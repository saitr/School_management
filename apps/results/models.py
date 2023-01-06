from django.db import models
from apps.subjects.models import StudentClass
from apps.students.models import Student
from django.urls import reverse
from django.contrib.postgres.fields import JSONField
from apps.subjects.models import Subject
# from apps.students.models import StudentMarks
# Create your models here.


    # declareresult = models.ForeignKey(DeclareResult, on_delete=models.SET_NULL)
    
class DeclareResult(models.Model):
    class Meta:
        db_table = 'Results'
    student_details = models.ForeignKey(Student,blank=True,null=True, on_delete=models.CASCADE,default=None)
    student_class = models.ForeignKey(StudentClass, blank=True,null=True, on_delete=models.CASCADE,)
    # student_marks = models.ForeignKey(StudentMarks,blank=True,null=True,related_name='related_result', on_delete=models.CASCADE)

    def student_marks(self):
        return self.related_result.all()

    # @property
    # def student_marks(self):
    #     return self.student_marks_details.all()
    # marks = models.OneToOneField(StudentMarks,unique=True, on_delete=models.DO_NOTHING,default=None)
    # marks = models.IntegerField('marks', null=True)
    # def __str__(self):
    #     return "%s Section-%s" % (self.select_class.class_name, self.select_class.section)


    # @property
    # def results_details(self):
    #     return self.related_results.all()

    # @property
    # def result_subjects(self):
    #     return self.related_sub.all()

class StudentMarks(models.Model):
    declareresult = models.ForeignKey(DeclareResult,related_name = 'related_result',null=True,on_delete=models.SET_NULL)
    student_subjects = models.ForeignKey(Subject,on_delete=models.CASCADE,default=None)
    marks = models.IntegerField('Marks')

    

    # @property
    # def marks(self):
    #     return self.related_result.all()
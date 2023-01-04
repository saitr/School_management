from django.db import models
from apps.subjects.models import StudentClass
# from apps.students.models import Student
from django.urls import reverse
from django.contrib.postgres.fields import JSONField
# from apps.subjects.models import Subject

# Create your models here.

class DeclareResult(models.Model):
    select_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    # subject = models.ForeignKey(Subject,related_name='related_sub', on_delete=models.CASCADE)
    # select_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.IntegerField('Marks', db_index=True, blank=True, null=True)
    # class Meta:
    #         unique_together = (( 'select_class'),)

    def __str__(self):
        return "%s Section-%s" % (self.select_class.class_name, self.select_class.section)


    @property
    def results_details(self):
        return self.related_results.all()

    @property
    def result_subjects(self):
        return self.related_sub.all()
    
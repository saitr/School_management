from django.db import models
from django.urls import reverse
# Create your models here.

class StudentClass(models.Model):
   
    class_name              =   models.CharField(max_length=100, primary_key=True, help_text='Eg- Third, Fouth,Sixth etc')
    section                 =   models.CharField(max_length=10, help_text='Eg- A,B,C etc')
    creation_date           =   models.DateTimeField(auto_now=False, auto_now_add=True)


    class Meta:
            unique_together = (('class_name', 'section'),)

            
    # def get_absolute_url(self):
    #     return reverse('student_classes:class_list')

    def __str__(self):
        return "%s Section-%s"%(self.class_name, self.section)

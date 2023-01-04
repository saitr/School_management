from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
title = (
    ('Mr','Mr' ),
    ('Ms', 'Ms'),
    ('Mrs', 'Mrs')
)
gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
)

class Admission_form(models.Model):
    class Meta:
        db_table = 'admission'
    title = models.CharField('title', max_length=20, choices=title)
    firstname = models.CharField('First Name',max_length=100,  db_index=True, blank=False, null = False )
    lastname = models.CharField('Last Name',max_length=100,  db_index=True, blank=False, null = False )
    email = models.EmailField('Email',max_length=500, blank=False, null=False)
    phone = models.IntegerField('Phone', blank=False, null=False)
    grade = models.CharField('Class', blank=False, null=False, max_length=100, db_index=True)
    gender = models.CharField('Gender', max_length=50, blank=False, null=False, choices=gender)
    father = models.CharField('Father Name',max_length=100, db_index=True, blank=True, null = True )
    mother = models.CharField('Mother Name',max_length=100, db_index=True, blank=True, null = True )
    gaurdian = models.CharField('Gaurdian Name',max_length=100, db_index=True, blank=True, null = True )
    adhaar = models.IntegerField('Aadhar', blank = False, null = False)
    domicile = models.IntegerField('Domicile Number', blank = False, null = False)
    photograph = CloudinaryField(
        'Photo', blank = True, null = True
    )
    signature = CloudinaryField(
        'Signature', blank = True, null = True
    )
    created_at = models.DateTimeField('CreatedAt', blank = False,auto_now_add=True)
    updated_at = models.DateTimeField('UpdatedAt',auto_now=True)

    def __str__(self):
        return self.Name


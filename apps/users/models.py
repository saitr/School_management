from django.db import models
# Create your models here.


class User(models.Model):
    class Meta(object):
        db_table = 'user'
    user_name = models.CharField(
        'Username', blank=False, null=False, db_index=True, max_length=50
    )
    employee_id = models.CharField(
        'Employee ID', blank=True, null=True, max_length=100, db_index=True
    )
    password = models.CharField(
        'Password', blank=False, null=False, db_index=True, max_length=255
    )
    email = models.EmailField(
        'Email', blank=False, null=False, db_index=True, max_length=100
    )
    token = models.CharField(
        'Token', blank=False, null=False, max_length=500
    )
    token_expires_at = models.DateTimeField(
        'Token Expires at', blank=False, null=False, max_length=50
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=False, auto_now=True
    )

    def __str__(self):
        return self.user_name

from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    image = models.FileField(upload_to='users/',null=True)

# image = models.FileField(upload_to='user_app/',null=True,default=None)

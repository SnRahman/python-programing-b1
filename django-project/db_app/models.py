from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15,null=True)
    email = models.CharField(max_length=255,null=True)


class Test_table(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

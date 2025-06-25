from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    dob = models.DateField()
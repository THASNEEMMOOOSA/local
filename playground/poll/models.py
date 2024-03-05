from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    city=models.CharField(max_length=100)
    dob=models.DateField()
    
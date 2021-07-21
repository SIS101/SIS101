from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)

class Programme(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
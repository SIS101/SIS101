from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, default="")

class Programme(models.Model):
    TYPE_CHOICES = [
        ('certificate', 'Certificate'),
        ('diploma', 'Diploma'),
        ('degree', 'Degree'),
        ('masters', 'Masters'),
        ('phd', 'Phd')
    ]
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, default="")
    type = models.CharField(max_length=200, choices=TYPE_CHOICES, default="diploma")
    field_work = models.BooleanField(default=False)
    practicals = models.BooleanField(default=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Course(models.Model):
    YEAR_CHOICES = [
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
        (5, 'Fifth Year'),
        (6, 'Sixth Year'),
        (7, 'Seventh Year')
    ]
    SEMESTER_CHOICES = [
        (1, 'First Semester'),
        (2, 'Second Semester'),
        (3, 'Third Semester')
    ]
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    year = models.IntegerField(choices=YEAR_CHOICES, default=1)
    semester = models.IntegerField(choices=SEMESTER_CHOICES, default=1)
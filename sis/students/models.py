from django.db import models
from admissions.models import Profile
from schools.models import Programme

class Student(models.Model):
    ADMISSION_TYPE_CHOICES = [
        ('undergraduate', 'Undergraduate'),
        ('diploma', 'Diploma'),
        ('degree', 'Degree'),
        ('masters', 'Masters'),
        ('phd', 'Phd')
    ]
    MODE_OF_STUDY = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('distance', 'Distance')
    ]
    QUALIFICATION_CHOICES = [
        ('high_school', 'Grade 12'),
        ('diploma', 'Diploma'),
        ('degree', 'Degree'),
        ('masters', 'Masters'),
        ('phd', 'Phd')
    ]
    SCHOOL_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('admitted', 'Admitted'),
        ('declined', 'Declined')
    ]
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    admission_type = models.CharField(max_length=200, choices=ADMISSION_TYPE_CHOICES, default="undergraduate")
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    highest_qualification = models.CharField(max_length=200, choices=QUALIFICATION_CHOICES, default="high_school")
    school_status = models.CharField(max_length=200, choices=SCHOOL_STATUS_CHOICES, default="pending")
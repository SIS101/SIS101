from django.db import models
from django.contrib.auth.models import User
from schools.models import School

class Profile(models.Model):
    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married')
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    PROFILE_TYPE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_type = models.CharField(max_length=200, choices=PROFILE_TYPE_CHOICES, default="student")
    other_names = models.CharField(max_length=200)
    marital_status = models.CharField(max_length=200, choices=MARITAL_STATUS_CHOICES, default="single")
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=200, default="zambia")
    national_id = models.CharField(max_length=200)

    province = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    physical_address = models.CharField(max_length=200)
    postal_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    next_of_kin_full_name = models.CharField(max_length=200)
    next_of_kin_email = models.EmailField(max_length=200)
    next_of_kin_phone = models.CharField(max_length=200)
    next_of_kin_province = models.CharField(max_length=200)
    next_of_kin_town = models.CharField(max_length=200)
    next_of_kin_physical_address = models.CharField(max_length=200)
    next_of_kin_postal_address = models.CharField(max_length=200)

class Staff(models.Model):
    POSITION_CHOICES = [
        ('lecturer', 'Lecturer'),
        ('accountant', 'Accountant'),
        ('vc', 'VC'),
        ('dvc', 'DVC'),
        ('other', 'Other')
    ]
    QUALIFICATION_CHOICES = [
        ('high_school', 'Grade 12'),
        ('diploma', 'Diploma'),
        ('degree', 'Degree'),
        ('masters', 'Masters'),
        ('phd', 'Phd')
    ]
    STATUS_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('distance', 'Distance')
    ]
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, choices=POSITION_CHOICES, default="undergraduate")
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="full_time")
    highest_qualification = models.CharField(max_length=200, choices=QUALIFICATION_CHOICES, default="high_school")
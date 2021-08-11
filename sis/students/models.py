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
    GRADE_CHOICES = [
        (0, "N/A"),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9)
    ]
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    admission_type = models.CharField(max_length=200, choices=ADMISSION_TYPE_CHOICES, default="undergraduate")
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    second_choice = models.CharField(max_length=200, null=True)
    third_choice = models.CharField(max_length=200, null=True)
    highest_qualification = models.CharField(max_length=200, choices=QUALIFICATION_CHOICES, default="high_school")
    
    secondary_school_attended = models.CharField(max_length=200, null=True)
    english_language = models.IntegerField(choices=GRADE_CHOICES, default=0)
    mathematics = models.IntegerField(choices=GRADE_CHOICES, default=0)
    biology = models.IntegerField(choices=GRADE_CHOICES, default=0)
    science = models.IntegerField(choices=GRADE_CHOICES, default=0)
    physics = models.IntegerField(choices=GRADE_CHOICES, default=0)
    chemistry = models.IntegerField(choices=GRADE_CHOICES, default=0)
    agricultural_science = models.IntegerField(choices=GRADE_CHOICES, default=0)
    history = models.IntegerField(choices=GRADE_CHOICES, default=0)
    commerce = models.IntegerField(choices=GRADE_CHOICES, default=0)
    civic_education = models.IntegerField(choices=GRADE_CHOICES, default=0)
    local_language = models.IntegerField(choices=GRADE_CHOICES, default=0)
    food_nutrition_and_home_management = models.IntegerField(choices=GRADE_CHOICES, default=0)
    religious_education = models.IntegerField(choices=GRADE_CHOICES, default=0)
    english_literature = models.IntegerField(choices=GRADE_CHOICES, default=0)
    principles_of_accounts = models.IntegerField(choices=GRADE_CHOICES, default=0)
    human_and_social_biology = models.IntegerField(choices=GRADE_CHOICES, default=0)
    geometric_and_mechanical_drawing = models.IntegerField(choices=GRADE_CHOICES, default=0)
    metal_work = models.IntegerField(choices=GRADE_CHOICES, default=0)
    geography = models.IntegerField(choices=GRADE_CHOICES, default=0)
    nutrition = models.IntegerField(choices=GRADE_CHOICES, default=0)
    wood_work = models.IntegerField(choices=GRADE_CHOICES, default=0)
    art = models.IntegerField(choices=GRADE_CHOICES, default=0)
    information_technology = models.IntegerField(choices=GRADE_CHOICES, default=0)

    #Uploads
    results_transcript = models.FileField(upload_to="student_uploads", null=True)
    nrc = models.FileField(upload_to="student_uploads", null=True)
    passport_photo = models.FileField(upload_to="student_uploads", null=True)

    school_status = models.CharField(max_length=200, choices=SCHOOL_STATUS_CHOICES, default="pending")

    def __str__(self) -> str:
        return self.profile.user.username
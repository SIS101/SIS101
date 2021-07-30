from django import forms
from schools.models import Programme

class ApplicationForm(forms.Form):

    #Personal details
    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married')
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    other_names = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={"class":"form-control"}))
    place_of_birth = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    nationality = forms.CharField(max_length=200, initial="zambia", widget=forms.TextInput(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, initial="male")
    national_id_or_passport = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOICES, initial="single", widget=forms.Select(attrs={"class":"form-control"}))

    #Address
    province = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    town = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    physical_address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    postal_address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))

    #Admissions
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
    
    admission_type = forms.ChoiceField(choices=ADMISSION_TYPE_CHOICES, initial="undergraduate", widget=forms.Select(attrs={"class":"form-control"}))
    first_choice = forms.ModelChoiceField(queryset=Programme.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    second_choice = forms.ModelChoiceField(queryset=Programme.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    third_choice = forms.ModelChoiceField(queryset=Programme.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    
    #Secondary
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
    secondary_school_attended = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    english_language = forms.ChoiceField(choices=GRADE_CHOICES)
    mathematics = forms.ChoiceField(choices=GRADE_CHOICES)
    biology = forms.ChoiceField(choices=GRADE_CHOICES)
    science = forms.ChoiceField(choices=GRADE_CHOICES)
    physics = forms.ChoiceField(choices=GRADE_CHOICES)
    chemistry = forms.ChoiceField(choices=GRADE_CHOICES)
    agricultural_science = forms.ChoiceField(choices=GRADE_CHOICES)
    history = forms.ChoiceField(choices=GRADE_CHOICES)
    commerce = forms.ChoiceField(choices=GRADE_CHOICES)
    civic_education = forms.ChoiceField(choices=GRADE_CHOICES)
    local_language = forms.ChoiceField(choices=GRADE_CHOICES)
    food_nutrition_and_home_management = forms.ChoiceField(choices=GRADE_CHOICES)
    religious_education = forms.ChoiceField(choices=GRADE_CHOICES)
    english_literature = forms.ChoiceField(choices=GRADE_CHOICES)
    principles_of_accounts = forms.ChoiceField(choices=GRADE_CHOICES)
    human_and_social_biology = forms.ChoiceField(choices=GRADE_CHOICES)
    geometric_and_mechanical_drawing = forms.ChoiceField(choices=GRADE_CHOICES)
    metal_work = forms.ChoiceField(choices=GRADE_CHOICES)
    geography = forms.ChoiceField(choices=GRADE_CHOICES)
    nutrition = forms.ChoiceField(choices=GRADE_CHOICES)
    wood_work = forms.ChoiceField(choices=GRADE_CHOICES)
    art = forms.ChoiceField(choices=GRADE_CHOICES)
    information_technology = forms.ChoiceField(choices=GRADE_CHOICES)

    #Uploads
    results_transcript = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}))
    nrc = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}))
    passport_photo = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}))

    #Next of kin
    next_of_kin_full_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_province = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_town = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_physical_address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_postal_address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))

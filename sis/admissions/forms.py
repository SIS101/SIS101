from django import forms
from schools.models import Programme

class ApplicationForm(forms.Form):
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
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))

    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOICES, initial="single", widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, initial="male")
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control"}, format="Y-m-d"))
    nationality = forms.CharField(max_length=200, initial="zambia", widget=forms.TextInput(attrs={"class":"form-control"}))
    national_id = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))

    province = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    town = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    physical_address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    postal_address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))

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

    PROGRAMME_CHOICES = []
    for a in Programme.objects.all():
        PROGRAMME_CHOICES.append((a.name, a.name))
    
    admission_type = forms.ChoiceField(choices=ADMISSION_TYPE_CHOICES, initial="undergraduate", widget=forms.Select(attrs={"class":"form-control"}))
    programme = forms.ChoiceField(choices=PROGRAMME_CHOICES)
    highest_qualification = forms.ChoiceField(choices=QUALIFICATION_CHOICES, initial="high_school", widget=forms.Select(attrs={"class":"form-control"}))

    next_of_kin_full_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_province = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_town = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_physical_address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))
    next_of_kin_postal_address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"form-control"}))

from django.db.models import fields
from django.forms import widgets
from . import models
from django import forms

class SchoolForm(forms.ModelForm):
    class Meta:
        model=models.School
        fields=["name", "code"]
        widgets={
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "code": forms.TextInput(attrs={"class": "form-control"})
        }

class ProgrammeForm(forms.ModelForm):
    class Meta:
        model=models.Programme
        fields=["name", "code", "type", "field_work", "practicals", "school"]
        widgets={
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "code": forms.TextInput(attrs={"class": "form-control"})
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model=models.Course
        fields=["name", "code", "year", "semester", "programme"]
        widgets={
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "code": forms.TextInput(attrs={"class": "form-control"})
        }
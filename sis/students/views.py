from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
@login_required
def students(request):
    template="dashboard/students/students.html"
    context={}

    students = models.Student.objects.filter(school_status="admitted")
    context["students"] = students

    return render(request, template, context)

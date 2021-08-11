from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
@login_required
def students(request):
    template="dashboard/students/students.html"
    context={}
    l_user = request.user
    context["l_user"]=l_user

    students = models.Student.objects.filter(school_status="admitted")
    context["students"] = students

    return render(request, template, context)

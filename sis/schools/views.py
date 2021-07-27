from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models, forms

# Create your views here.
@login_required
def index(request):
    template="dashboard/schools/index.html"
    context={}

    schools = models.School.objects.all()
    context["schools"]=schools

    return render(request, template, context)

@login_required
def add_school(request):
    template="dashboard/schools/add-school.html"
    context={}

    form = forms.SchoolForm()
    context["form"]=form

    if request.method == "POST":
        pform = forms.SchoolForm(request.POST)
        if pform.is_valid():
            pform.save()
            messages.success(request, "School successfully added!")
        else:
            messages.error(request, "Failed to add school.")
            context["form"]=pform

    return render(request, template, context)

@login_required
def view_school(request, school_id):
    template="dashboard/schools/view-school.html"
    context={}

    school = models.School.objects.get(pk=school_id)
    programmes = models.Programme.objects.filter(school=school)
    context["school"]=school
    context["programmes"]=programmes

    return render(request, template, context)

@login_required
def add_programme(request, school_id):
    template="dashboard/schools/add-programme.html"
    context={}

    school = models.School.objects.get(pk=school_id)
    context["school"]=school
    form = forms.ProgrammeForm({"school": school_id})
    context["form"]=form

    if request.method == "POST":
        pform = forms.ProgrammeForm(request.POST)
        if pform.is_valid():
            pform.save()
            messages.success(request, "Programme successfully added!")
        else:
            messages.error(request, "Failed to add programme.")
            context["form"]=pform

    return render(request, template, context)

@login_required
def view_programme(request, programme_id):
    template="dashboard/schools/view-programme.html"
    context={}

    programme = models.Programme.objects.get(pk=programme_id)
    context["programme"]=programme
    courses=models.Course.objects.filter(programme=programme)
    context["courses"]=courses

    return render(request, template, context)

def add_course(request, programme_id):
    template="dashboard/schools/add-course.html"
    context={}

    form = forms.CourseForm({"programme":programme_id})
    context["form"]=form
    programme = models.Programme.objects.get(pk=programme_id)
    context["programme"]=programme

    if request.method == "POST":
        pform = forms.CourseForm(request.POST)
        if pform.is_valid():
            pform.save()
            messages.success(request, "Course successfully added!")
        else:
            messages.error(request, "Failed to add Course.")
            context["form"]=pform

    return render(request, template, context)

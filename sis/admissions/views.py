from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import ApplicationForm
from portal.forms import UserForm
from students.forms import StudentForm
from . import forms, models
from schools.models import Programme
from django.utils import timezone
from students.models import Student

# Create your views here.
@login_required
def index(request):
    template="dashboard/admissions/index.html"
    context={}

    return render(request, template, context)

@login_required
def my_application(request):
    template="dashboard/admissions/my-application.html"
    context={}
    l_user = request.user
    context["l_user"] = request.user

    return render(request, template, context)

@login_required
def applicants(request):
    template="dashboard/admissions/applicants.html"
    context={}
    l_user = request.user
    context["l_user"] = request.user

    applicants_list = Student.objects.filter(school_status="pending")
    context["applicants"]=applicants_list

    return render(request, template, context)

@login_required
def view_applicant(request, applicant_id):
    template="dashboard/admissions/view-applicant.html"
    context={}
    l_user = request.user
    context["l_user"] = request.user

    applicant = Student.objects.get(pk=applicant_id)
    context["applicant"]=applicant

    return render(request, template, context)

@login_required
def handle_applicant(request, applicant_id, action):
    try:
        applicant = Student.objects.get(pk=applicant_id)
        applicant.school_status = action
        applicant.save()
    except Exception as e:
        messages.error(request, e)
    else:
        messages.success(request, "Success!")

    return redirect(reverse("admissions:applicants"))

def application(request):
    template="website/application.html"
    context={}

    application_form = ApplicationForm()
    context["application_form"] = application_form

    if request.method == "POST":
        application = ApplicationForm(request.POST, request.FILES)
        if application.is_valid():
            data = application.cleaned_data

            data["username"] = data["email"]
            data["date_joined"] = timezone.datetime.today()
            data["password"] = "123456"
            new_user = UserForm(data)
            if new_user.is_valid():
                saved_user = new_user.save()
                messages.success(request, "Account created successfully.")

                try:
                    saved_user.set_password("123456")
                    saved_user.is_active=True
                    saved_user.profile.other_names = data["other_names"]
                    saved_user.profile.marital_status = data["marital_status"]
                    saved_user.profile.gender=data["gender"]
                    saved_user.profile.date_of_birth=data["date_of_birth"]
                    saved_user.profile.nationality=data["nationality"]
                    saved_user.profile.national_id=data["national_id_or_passport"]
                    saved_user.profile.province=data["province"]
                    saved_user.profile.town=data["town"]
                    saved_user.profile.physical_address=data["physical_address"]
                    saved_user.profile.postal_address=data["postal_address"]
                    saved_user.profile.phone=data["phone"]
                    saved_user.profile.next_of_kin_full_name=data["next_of_kin_full_name"]
                    saved_user.profile.next_of_kin_email=data["next_of_kin_email"]
                    saved_user.profile.next_of_kin_phone=data["next_of_kin_phone"]
                    saved_user.profile.next_of_kin_province=data["next_of_kin_province"]
                    saved_user.profile.next_of_kin_town=data["next_of_kin_town"]
                    saved_user.profile.next_of_kin_physical_address=data["next_of_kin_physical_address"]
                    saved_user.profile.next_of_kin_postal_address=data["next_of_kin_postal_address"]

                    saved_user.save()
                except Exception as e:
                    messages.warning(request, e)
                else:
                    messages.success(request, "Profile created successfully.")

                    data["profile"]=saved_user.profile.pk
                    data["programme"]=Programme.objects.get(name=data["first_choice"])
                    data["highest_qualification"]="high_school"
                    data["school_status"]="pending"
                    student_form = StudentForm(data=data, files=application.files)
                    if student_form.is_valid():
                        student_form.save()
                        messages.success(request, "Student successfully created.")
                        messages.success(request, "Login username: {}, password: 123456".format(data["email"]))
                        return redirect("/admissions/application/success")
                    else:
                        messages.warning(request, student_form.errors)
            else:
                messages.warning(request, new_user.errors)
        else:
            context["application_form"] = application

    return render(request, template, context)

def application_success(request):
    template="website/application_success.html"
    context={}

    return render(request, template, context)

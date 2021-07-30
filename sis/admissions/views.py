from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .forms import ApplicationForm
from portal.forms import UserForm
from datetime import date

# Create your views here.
def index(request):
    template="dashboard/base.html"
    context={}

    return render(request, template, context)

def application(request):
    template="website/application.html"
    context={}

    application_form = ApplicationForm()
    context["application_form"] = application_form

    if request.method == "POST":
        application = ApplicationForm(request.POST, request.FILES)
        if application.is_valid():
            student_group = Group.objects.get(name="student")
            data = application.cleaned_data
            data["username"] = data["national_id_or_passport"]
            data["date_joined"] = date.today()
            data["password"] = "123456"
            new_user = UserForm(data)
            if new_user.is_valid():
                new_user.save()
                new_user.instance.groups.add(student_group.pk)
                new_user.instance.save()
                student_group.user_set.add(new_user.instance)
                print(new_user.instance)
            else:
                print(new_user.errors)
            print("me")
        else:
            context["application_form"] = application

    return render(request, template, context)
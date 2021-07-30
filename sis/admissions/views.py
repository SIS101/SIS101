from django.shortcuts import render
from django.contrib import messages
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
            data = application.cleaned_data
            data["username"] = data["national_id_or_passport"]
            data["date_joined"] = date.today()
            data["password"] = "123456"
            new_user = UserForm(data)
            if new_user.is_valid():
                new_user.save()
                new_user.instance.save()
                messages.success(request, "Your application was successfully submitted")
            else:
                print(new_user.errors)
            print("me")
        else:
            context["application_form"] = application

    return render(request, template, context)
from django.shortcuts import render
from .forms import ApplicationForm

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
        application = ApplicationForm(request.POST)
        if application.is_valid():
            data = application.cleaned_data
            print(data)
        else:
            context["application_form"] = application

    return render(request, template, context)
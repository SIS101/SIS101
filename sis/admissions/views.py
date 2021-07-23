from django.shortcuts import render

# Create your views here.
def index(request):
    template="dashboard/base.html"
    context={}

    return render(request, template, context)

def application(request):
    template="website/application.html"
    context={}

    return render(request, template, context)
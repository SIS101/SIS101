from django.shortcuts import render

# Create your views here.
def home(request):
    template = "website/home.html"
    context = {}

    return render(request, template, context)
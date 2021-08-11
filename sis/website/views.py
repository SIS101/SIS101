from django.contrib import messages
from django.shortcuts import render
from schools.models import Programme
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    template = "website/home.html"
    context = {}

    return render(request, template, context)

def our_programmes(request):
    template="website/programmes.html"
    context={}

    programmes = Programme.objects.all().order_by("pk")
    programme_paginator = Paginator(programmes, 2)

    page_index = request.GET["page"]
    context["programmes"]=programme_paginator.get_page(page_index)

    return render(request, template, context)

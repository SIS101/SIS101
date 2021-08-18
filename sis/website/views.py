from django import forms
from django.contrib import messages
from django.shortcuts import render
from schools.models import Programme
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models

def home(request):
    template = "website/home.html"
    context = {}
    try:
        websiteSetting = models.WebsiteSetting.objects.get(pk=1)
    except:
        return HttpResponseRedirect(reverse("portal:initial-setup"))

    programmes = Programme.objects.all()
    context["programmes"]=programmes

    return render(request, template, context)

def our_programmes(request):
    template="website/programmes.html"
    context={}

    programmes = Programme.objects.all().order_by("pk")
    programme_paginator = Paginator(programmes, 2)

    page_index = request.GET["page"]
    context["programmes"]=programme_paginator.get_page(page_index)

    return render(request, template, context)

def view_programme(request, pk):
    template="website/programmes.html"
    context={}

    return render(request, template, context)

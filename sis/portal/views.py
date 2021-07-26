from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def dashboard(request):
    template="dashboard/base.html"
    context={}

    return render(request, template, context)

# Create your views here.
def login_page(request):
    template="dashboard/login.html"
    context={}

    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome %s' % request.user.get_username())
            if request.POST['next'] != 'None':
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('portal:dashboard'))
        else:
            messages.error(request, 'ID or Password incorrect')
            return HttpResponseRedirect(reverse('portal:login'))
    else:
        context["next"]="/"

    return render(request, template, context)

def logout_user(request):
    logout(request)
    messages.warning(request, 'You have logged out!')
    return HttpResponseRedirect(reverse('portal:login'))
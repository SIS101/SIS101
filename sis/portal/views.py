from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from website.models import WebsiteSetting
from website.forms import WebsiteSettingForm

@login_required
def dashboard(request):
    template="dashboard/portal/dashboard.html"
    context={}
    l_user=request.user
    context["l_user"]=l_user

    return render(request, template, context)

# Create your views here.
def login_page(request):
    template="dashboard/login.html"
    context={}

    try:
        next = request.GET["next"]
    except:
        next = None

    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome %s' % request.user.get_username())
            if next != None:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(reverse('portal:dashboard'))
        else:
            messages.error(request, 'ID or Password incorrect')
            return HttpResponseRedirect(reverse('portal:login'))
    
    elif request.user.is_authenticated:
        if next != None:
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect(reverse('portal:dashboard'))

    return render(request, template, context)

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, 'You have logged out!')
    return HttpResponseRedirect(reverse('portal:login'))

def coming_soon(request):
    template="dashboard/coming-soon.html"
    context={}

    return render(request, template, context)

@login_required
def initial_setup(request):
    template="dashboard/initial-setup.html"
    context={}

    l_user=request.user
    context["l_user"]=l_user
    
    if l_user.has_perm("website.view_websiteSetting"):
        
        context["form"]=WebsiteSettingForm()

        if request.method == "POST":
            form = WebsiteSettingForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("website:home"))
            else:
                context["form"]=form

        return render(request, template, context)
    else:
    
        messages.warning(request, "Access denied.")
        return HttpResponseRedirect(reverse("portal:dashboard"))
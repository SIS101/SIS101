from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def payments(request):
    template="dashboard/payments/payments.html"
    context={}
    l_user=request.user
    context["l_user"]=l_user

    return render(request, template, context)

@login_required
def due(request):
    template="dashboard/payments/due.html"
    context={}
    l_user=request.user
    context["l_user"]=l_user

    return render(request, template, context)
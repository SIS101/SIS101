from django.shortcuts import render

# Create your views here.
def payments(request):
    template="dashboard/payments/payments.html"
    context={}
    l_user=request.user
    context["l_user"]=l_user

    return render(request, template, context)

def due(request):
    template="dashboard/payments/due.html"
    context={}
    l_user=request.user
    context["l_user"]=l_user

    return render(request, template, context)
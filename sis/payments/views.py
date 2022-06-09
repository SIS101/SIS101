from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from payments import models, forms
from payments.DataTypes import StudentBalance

# Create your views here.
@login_required
def payments(request):
    template="dashboard/payments/payments.html"
    context={}
    l_user=request.user
    context["l_user"]=l_user

    payments = models.StudentDeposit.objects.filter(student=l_user.profile.student)
    context["payments"] = payments

    bs = StudentBalance(l_user.profile.student)
    context["balance"] = bs

    return render(request, template, context)

@login_required
def payment(request, payment_id):
    template="dashboard/payments/payment.html"
    context={}
    l_user=request.user
    context["l_user"]=l_user

    payment = models.StudentDeposit.objects.get(pk=payment_id)
    context["payment"] = payment

    return render(request, template, context)

@login_required
def pending(request):
    template="dashboard/payments/pending.html"
    context={}
    l_user=request.user
    context["l_user"]=l_user

    invoices = models.Invoice.objects.filter(to=l_user.profile.student)
    context["invoices"] = invoices

    return render(request, template, context)

@login_required
def invoice(request, invoice_id):
    template="dashboard/payments/invoice.html"
    context={}
    l_user=request.user
    context["l_user"]=l_user

    invoice = models.Invoice.objects.get(pk=invoice_id)
    context["invoice"] = invoice

    bs = StudentBalance(l_user.profile.student)
    context["balance"] = bs

    clearInvoice = request.GET.get("clear",None)
    if not clearInvoice == None:
        if bs.total_balance < 0:
            return HttpResponseRedirect(reverse("payments:submit-deposit-slip"))
        else:
            invoice.status = "cleared"
            invoice.save()

    return render(request, template, context)

@login_required
def submit_deposit_slip(request):
    template="dashboard/payments/submit-deposit-slip.html"
    context={}
    l_user=request.user
    context["l_user"]=l_user
    context["form"] = forms.StudentDepositForm()

    if request.method == "POST":
        form = forms.StudentDepositForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data["student"] = l_user.profile.student
            data["status"] = "pending"
            models.StudentDeposit.objects.create(**data)
            messages.success(request, "Deposit slip successfully submitted!")
            return HttpResponseRedirect(reverse("payments:payments"))
        else:
            context["form"] = form
            messages.error(request, "Failed to submit form")

    return render(request, template, context)
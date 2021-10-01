from django import forms
from . import models

class StudentDepositForm(forms.ModelForm):
    class Meta:
        model=models.StudentDeposit
        fields=["transaction_id", "description", "amount", "deposit_date"]
        widgets={
            "transaction_id": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.TextInput(attrs={"class": "form-control"}),
            "deposit_date": forms.TextInput(attrs={"class": "form-control"}),
        }
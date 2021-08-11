from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Invoice(models.Model):
    to = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    due_date = models.DateField()
    notes = models.TextField(blank=True, default="")

    def __str__(self):
        return self.to.username+"->"+str(self.get_total())

    def get_total(self):
        total = 0
        items = InvoiceItem.objects.filter(invoice=self)
        for item in items:
            total += item.amount
        return total

class InvoiceItem(models.Model):
    invoice=models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    amount=models.FloatField()

    def __str__(self):
        return self.description


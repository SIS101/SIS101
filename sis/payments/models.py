from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from students.models import Student

# Create your models here.
class Invoice(models.Model):
    STATUS_CHOICES=[
        ('pending', 'PENDING'),
        ('cleared', 'CLEARED')
    ]
    to = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    due_date = models.DateField()
    notes = models.TextField(blank=True, default="")
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return self.to.profile.user.username+"-K"+str(self.get_total())+"->"+self.status

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
"""
class Deposit(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)

"""
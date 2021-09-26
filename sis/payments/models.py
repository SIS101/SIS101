from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from students.models import Student
from schools.models import Programme

# Create your models here.
class ProgrammeFee(models.Model):
    programme=models.OneToOneField(Programme, on_delete=models.CASCADE)
    amount=models.FloatField(default=0.0)

    def __str__(self):
        return str(self.amount)

    @receiver(post_save, sender=Programme)
    def on_create_programme(instance, created, **kwargs):
        if created:
            ProgrammeFee.objects.create(programme=instance)

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
        
class StudentDeposit(models.Model):
    STATUS_CHOICE=[
        ('pending', 'PENDING'),
        ('accepted', 'ACCEPTED'),
        ('declined', 'DECLINED')
    ]
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    transaction_id=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    amount=models.FloatField()
    deposit_date=models.DateField()
    status=models.CharField(max_length=200, choices=STATUS_CHOICE)

    def __str__(self):
        return self.student.profile.user.username+"-"+self.transaction_id+"-"+str(self.amount)

class StudentBalance(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    balance=models.FloatField()
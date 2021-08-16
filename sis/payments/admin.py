from django.contrib import admin
from . import models

admin.site.register(models.Invoice)
admin.site.register(models.InvoiceItem)
admin.site.register(models.StudentDeposit)
admin.site.register(models.StudentBalance)
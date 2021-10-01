from django.urls import path
from . import views

app_name="payments"
urlpatterns = [
    path('', views.payments, name="payments"),
    path('payment/<payment_id>', views.payment, name="payment"),
    path('pending/', views.pending, name="pending"),
    path('invoice/<invoice_id>', views.invoice, name="invoice"),
    path('submit-deposit-slip/', views.submit_deposit_slip, name="submit-deposit-slip"),
]

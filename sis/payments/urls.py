from django.urls import path
from . import views

app_name="payments"
urlpatterns = [
    path('', views.payments, name="payments"),
    path('due/', views.due, name="due"),
]

from django.urls import path
from . import views

app_name="portal"
urlpatterns = [
    path('login/', views.login_page, name="login")
]

from django.urls import path
from . import views

app_name="website"
urlpatterns = [
    path('', views.home, name="home"),
    path('our-programmes/', views.our_programmes, name="our-programmes")
]

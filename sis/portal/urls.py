from django.urls import path
from . import views

app_name="portal"
urlpatterns = [
    path('coming-soon/', views.coming_soon, name="coming-soon"),
    path('initial-setup/', views.initial_setup, name="initial-setup"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard")
]

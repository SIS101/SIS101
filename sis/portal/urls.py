from django.urls import path
from . import views

app_name="portal"
urlpatterns = [
    path('programmes', views.programmes, name="programmes"),
    path('coming-soon/', views.coming_soon, name="coming-soon"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('', views.dashboard, name="dashboard")
]

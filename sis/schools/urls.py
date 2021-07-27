from django.urls import path
from . import views

app_name="schools"
urlpatterns = [
    path('', views.index, name="index"),
    path('add-school/', views.add_school, name="add-school"),
    path('view-school/<school_id>', views.view_school, name="view-school"),
    path('add-programme/<school_id>', views.add_programme, name="add-programme"),
    path('view-programme/<programme_id>', views.view_programme, name="view-programme"),
    path('add-course/<programme_id>', views.add_course, name="add-course")
]

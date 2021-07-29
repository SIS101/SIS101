from django.urls import path
from . import views

app_name="schools"
urlpatterns = [
    path('', views.index, name="index"),
    path('add-school/', views.add_school, name="add-school"),
    path('view-school/<school_id>', views.view_school, name="view-school"),
    path('add-programme/<school_id>', views.add_programme, name="add-programme"),
    path('view-programme/<programme_id>', views.view_programme, name="view-programme"),
    path('add-course/<programme_id>', views.add_course, name="add-course"),
    path('edit-course/<programme_id>/<course_id>', views.edit_course, name="edit-course"),
    path('delete/<object_type>/<object_id>', views.delete_object, name="delete")
]

from django.urls import path
from . import views

app_name="admissions"
urlpatterns = [
    path('', views.index, name='index'),
    path('application/', views.application, name="application"),
    path('application/success/', views.application_success, name="application-success"),
    path('applicants/', views.applicants, name="applicants"),
    path('applicant/<applicant_id>/', views.view_applicant, name="view-applicant"),
    path('applicant/<int:applicant_id>/<str:action>', views.handle_applicant, name="handle-applicant"),
]

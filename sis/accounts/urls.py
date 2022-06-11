from django.urls import path
from accounts import views

app_name="accounts"
urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("student-deposit/pending",views.PendingStudentDeposit.as_view(),name="pending-student-deposit"),
    path("student-deposit/accepted",views.AcceptedStudentDeposit.as_view(),name="accepted-student-deposit"),
    path("student-deposit/declined",views.DeclinedStudentDeposit.as_view(),name="declined-student-deposit"),
    path("student-deposit/<int:pk>/",views.StudentDepositDetail.as_view(),name="student-deposit-detail"),
    path("student-deposit/<int:pk>/update",views.UpdateStudentDeposit.as_view(),name="update-student-deposit"),
]
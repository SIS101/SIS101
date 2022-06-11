from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView
from django.utils.decorators import method_decorator
from payments.models import StudentDeposit

# Create your views here.
@method_decorator(login_required,name="dispatch")
class StudentDepositDetail(PermissionRequiredMixin,DetailView):
    permission_required=("payments.view_studentdeposit")
    model=StudentDeposit
    context_object_name="deposit"
    template_name="dashboard/accounts/student-deposits-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["l_user"] = self.request.user
        return context

@method_decorator(login_required,name="dispatch")
class IndexView(PermissionRequiredMixin,ListView):
    permission_required=("payments.view_studentdeposit")
    template_name="accounts/accounts.html"
    model = StudentDeposit
    context_object_name="deposits"
    paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["l_user"] = self.request.user
        return context

@method_decorator(login_required,name="dispatch")
class UpdateStudentDeposit(PermissionRequiredMixin,UpdateView):
    permission_required=("payments.change_studentdeposit")
    template_name="accounts/update-student-deposit.html"
    model=StudentDeposit
    context_object_name="deposit"
    fields=["status"]
    success_url="/accounts/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["l_user"] = self.request.user
        return context

@method_decorator(login_required,name="dispatch")
class PendingStudentDeposit(PermissionRequiredMixin,ListView):
    permission_required=("payments.view_studentdeposit")
    template_name="accounts/pending-student-deposit.html"
    queryset=StudentDeposit.objects.filter(status="pending")
    context_object_name="deposits"
    paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["l_user"] = self.request.user
        return context

@method_decorator(login_required,name="dispatch")
class AcceptedStudentDeposit(PermissionRequiredMixin,ListView):
    permission_required=("payments.view_studentdeposit")
    template_name="accounts/accepted-student-deposit.html"
    queryset=StudentDeposit.objects.filter(status="accepted")
    context_object_name="deposits"
    paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["l_user"] = self.request.user
        return context

@method_decorator(login_required,name="dispatch")
class DeclinedStudentDeposit(PermissionRequiredMixin,ListView):
    permission_required=("payments.view_studentdeposit")
    template_name="accounts/declined-student-deposit.html"
    queryset=StudentDeposit.objects.filter(status="declined")
    context_object_name="deposits"
    paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["l_user"] = self.request.user
        return context
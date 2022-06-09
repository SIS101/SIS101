from payments.models import (
    Invoice,
    StudentDeposit
)

class StudentBalance:
    def __init__(self,student):
        self.invoices = Invoice.objects.filter(to=student)
        self.deposits = StudentDeposit.objects.filter(student=student,status="accepted")
    
    @property
    def total_credit(self) -> float:
        t = 0
        for inv in self.invoices:
            t += inv.total
        
        return t
    
    @property
    def total_debit(self) -> float:
        t = 0
        for dep in self.deposits:
            t += dep.amount

        return t
    
    @property
    def total_balance(self) -> float:
        return self.total_debit - self.total_credit
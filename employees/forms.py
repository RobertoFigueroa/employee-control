from django import forms
from employees.models import Employee
from departments.models import Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        department = forms.ModelChoiceField(queryset=Department.objects.all())
        fields = ["names", "last_names", "date", "department"]

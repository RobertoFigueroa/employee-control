from django import forms
from departments.models import Department

class DeptForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["code", "name", "description"]

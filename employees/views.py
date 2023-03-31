from django.shortcuts import render, redirect

from django.http import HttpResponse

from employees.models import Employee
from employees.forms import EmployeeForm
from departments.models import Department


def index(request):
    # Traer tabla de empleados
    employees = Employee.objects.all()
    # Mostrar tabla de empleados
    return render(request, "employees.html", {'employees' : employees})
# Create your views here.


def edit(request, code):
    employee = Employee.objects.get(code=code)
    depts = Department.objects.all()
    return render(request, "edit_employee.html", {'employee' : employee, 'depts' : depts})

def update(request, code):
    employee = Employee.objects.get(code=code)

    #dept_code = request.POST.get("department")
    #dept = Department.objects.get(code=dept_code)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            try:
                # obj = form.save(commit=False)
                # related_object = form.cleaned_data['department']
                # obj.related_field = related_object
                # obj.save()
                form.save()
                return redirect("/")
            except:
                print("FORM COULD NOT BE SAVED")
        else:
            form.non_field_errors()
            field_errors = [ (field.label, field.errors) for field in form]
            print(field_errors) 
            return render(request, 'edit_employee.html', {'employee': employee})
        

def delete(request, code):
    employee = Employee.objects.get(code=code)
    employee.delete()
    return redirect("/")


def create(request):
    depts = Department.objects.all()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                print("COULD NOT SAVE FORM")
        else:
            form.non_field_errors()
            field_errors = [ (field.label, field.errors) for field in form]
            print(field_errors) 
            form = EmployeeForm()
            return render(request, 'create_employee.html', {'employee':form, 'depts' : depts})
    else:
        form = EmployeeForm()
        return render(request, 'create_employee.html', {'employee':form, 'depts' : depts})

from django.shortcuts import render, redirect

from django.http import HttpResponse

from employees.models import Employee
from departments.models import Department
from departments.forms import DeptForm

def index(request):
    # Traer tabla de empleados
    depts = Department.objects.all()
    # Mostrar tabla de empleados
    return render(request, "depts.html", {'depts' : depts})
# Create your views here.


def edit(request, code):
    dept = Department.objects.get(code=code)
    return render(request, "edit_dept.html", {'dept' : dept})

def update(request, code):
    dept = Department.objects.get(code=code)

    #dept_code = request.POST.get("department")
    #dept = Department.objects.get(code=dept_code)
    if request.method == "POST":
        form = DeptForm(request.POST, instance=dept)
        if form.is_valid():
            try:
                # obj = form.save(commit=False)
                # related_object = form.cleaned_data['department']
                # obj.related_field = related_object
                # obj.save()
                form.save()
                return redirect("/depts")
            except:
                print("FORM COULD NOT BE SAVED")
        else:
            form.non_field_errors()
            field_errors = [ (field.label, field.errors) for field in form]
            print(field_errors) 
            return render(request, 'edit_dept.html', {'dept': dept})
        

def delete(request, code):
    dept = Department.objects.get(code=code)
    dept.delete()
    return redirect("/depts")


def create(request):
    depts = Department.objects.all()
    if request.method == "POST":
        form = DeptForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/depts")
            except:
                print("COULD NOT SAVE FORM")
        else:
            form.non_field_errors()
            field_errors = [ (field.label, field.errors) for field in form]
            print(field_errors) 
            form = DeptForm()
            return render(request, 'create_dept.html', {'employee':form, 'depts' : depts})
    else:
        form = DeptForm()
        return render(request, 'create_dept.html', {'employee':form, 'depts' : depts})

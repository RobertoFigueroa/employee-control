from django.db import models

from departments.models import Department

class Employee(models.Model):
    code = models.CharField(max_length=12, primary_key=True, editable=False)
    names = models.CharField(max_length=100, null=False)
    last_names = models.CharField(max_length=100, null=False)
    date = models.DateField(blank=True, null=True)
    department = models.ForeignKey(Department)

    def save(self, *args, **kwargs):
        latest_emp = Employee.objects.all().order_by("code").first()
        if latest_emp:
            serial_number = int(latest_emp.code[4:]) +1
        else:
            serial_number = 1

        self.code = 'EMP-{:04d}'.format(serial_number)

        super(Employee, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Employees"


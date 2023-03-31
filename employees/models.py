from django.db import models

from departments.models import Department

class Employee(models.Model):
    code = models.CharField(max_length=12, editable=False)
    names = models.CharField(max_length=100, null=False)
    last_names = models.CharField(max_length=100, null=False)
    date = models.DateField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def save(self, *args, **kwargs): 
        if not self.code:
            latest_emp = Employee.objects.all().order_by("-code").first()
            serial_number = 1
            if latest_emp:
                print("This is last", latest_emp)
                serial_number = int(latest_emp.code[4:]) +1

            self.code = 'EMP-{:04d}'.format(serial_number)

        super(Employee, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "Employees"



from django.db import models

class Department(models.Model):

    code = models.CharField(max_length=12, null=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, default='', blank=True)

    # def save(self, *args, **kwargs):
    #     dept_code = Department.objects.get(code=self.code)
    #     if dept_code:
    #         super(Department, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Departments"



from django.db import models


# Create your models here.
class EmployeesTBL(models.Model):
    emp_name = models.CharField(max_length=30)
    emp_salary = models.CharField(max_length=20)
    emp_city = models.CharField(max_length=30)
    emp_dob = models.DateField()
    emp_mobile_no = models.CharField(max_length=10)

    def __str__(self):
        return self.emp_name

    class Meta:
        db_table = 'EmployeesTBL'

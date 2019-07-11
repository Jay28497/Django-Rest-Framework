from django.db import models


# Create your models here.
class Employees(models.Model):
    emp_id = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


    def __str__(self):
        return self.first_name

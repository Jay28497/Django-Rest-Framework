from django.db import models


# Create your models here.
class CustomerTBL(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_salary = models.CharField(max_length=20)
    customer_city = models.CharField(max_length=30)
    customer_mobile_no = models.CharField(max_length=10)

    def __str__(self):
        return self.customer_name

    class Meta:
        db_table = 'CustomerTBL'

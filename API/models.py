from django.db import models


# Create your models here.
class ProductTBL(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.CharField(max_length=30)
    product_quantity = models.CharField(max_length=30)
    product_details = models.CharField(max_length=150)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'ProductTBL'

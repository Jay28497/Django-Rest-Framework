from rest_framework import serializers
from API.models import ProductTBL


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTBL
        fields = ('id',
                  'product_name',
                  'product_price',
                  'product_quantity',
                  'product_details')

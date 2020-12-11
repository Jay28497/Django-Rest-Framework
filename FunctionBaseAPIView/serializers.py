from rest_framework import serializers
from FunctionBaseAPIView.models import CustomerTBL


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerTBL
        fields = ('id',
                  'customer_name',
                  'customer_salary',
                  'customer_city',
                  'customer_mobile_no')

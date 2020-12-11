from rest_framework import serializers
from ClassBaseAPIView.models import EmployeesTBL


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesTBL
        fields = ('id',
                  'emp_name',
                  'emp_salary',
                  'emp_city',
                  'emp_dob',
                  'emp_mobile_no')

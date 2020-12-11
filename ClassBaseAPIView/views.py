from rest_framework import viewsets
from ClassBaseAPIView.serializers import EmployeesSerializer
from ClassBaseAPIView.models import EmployeesTBL


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeesTBL.objects.all()
    serializer_class = EmployeesSerializer

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import employeesSerializer


# Create your views here.
class employeeList(APIView):

    def get(self, request):
        emp = Employees.objects.all()
        serializer = employeesSerializer(emp, many=True)
        return Response(serializer.data)


    def post(self):
        pass
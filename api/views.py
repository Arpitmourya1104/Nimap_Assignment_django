from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSErializer
# Create your views here.
class CompanyViewSEt(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class= CompanySerializer

class EmployeeViewSEt(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSErializer


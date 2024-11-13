from django.shortcuts import HttpResponse
from home.models import Company
from .serializers import CompanySerializer
from .serializers import EmployeeSerializer
from rest_framework import generics
from home.models import Employee
# Create your views here.

def index(request):
    return HttpResponse("Welcome to the Student API. Go to /api/students/ to see the student list.")

class CompanyListCreateview(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'


class EmployeListCreateview(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


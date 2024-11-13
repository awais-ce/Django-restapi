from rest_framework import serializers
from home.models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id' , 'name' ,'address' ,'city', 'state', 'country', 'companytype', 'website']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'company', 'position', 'salary', 'joinning_date']





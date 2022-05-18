from crud.models import Employee, Division
from rest_framework import serializers


class DivisionCreatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ("division_name",)


class DivisionListandDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d %B %Y %H:%M:%S")
    class Meta:
        model = Division
        fields = ("id", "division_name", "created_at")

class EmployeeCreatedSerializer(serializers.ModelSerializer):
    hire_date = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Employee
        fields = ("first_name", "last_name", "address", "hire_date", "division")
    
class EmployeeSerializer(serializers.ModelSerializer):
    hire_date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%d %B %Y %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%d %B %Y %H:%M:%S")
    division = DivisionListandDetailSerializer(many=False)
    class Meta:
        model = Employee
        fields = ("id","first_name", "last_name", "address", "created_at", "updated_at", "hire_date", "division")
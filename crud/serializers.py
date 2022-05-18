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
    class Meta:
        model = Employee
        fields = ("id", "first_name", "last_name", "address", "hire_date", "divison")

class EmployeeSerializer(serializers.ModelSerializer):
    hire_date = serializers.DateField(format="%Y-%m-%d")
    division = DivisionCreatedSerializer(many=True)
    class Meta:
        model = Employee
        fields = ("id","first_name", "last_name", "address", "created_at", "updated_at", "hire_date", "division")
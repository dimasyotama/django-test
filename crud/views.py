from django.shortcuts import render
from crud.models import Division, Employee
from crud.serializers import DivisionListandDetailSerializer, EmployeeSerializer, DivisionCreatedSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework.settings import api_settings


@api_view(["GET"])
def divisionList(request):
    division_query = Division.objects.all().order_by("id")
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    paginator = pagination_class()
    page = paginator.paginate_queryset(division_query, request)
    serializer = DivisionListandDetailSerializer(page, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def division_detail(request, pk):
    division_query = Division.objects.get(id=pk)
    serializer = DivisionListandDetailSerializer(division_query, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def create_division(request):
    serializer = DivisionCreatedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(["POST"])
def update_division(request, pk):
    division_query = Division.objects.get(id=pk)
    serializer = DivisionCreatedSerializer(instance=division_query, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(["DELETE"])
def delete_division(request, pk):
    division_query = Division.objects.get(id=pk)
    division_query.delete()
    content = {"status":"Data Has been deleted"}
    return Response(content, status=status.HTTP_200_OK)
        

    
@api_view(["GET"])
def employee_list(request):
    employee_query = Employee.objects.all().order_by("id")
    serializer = EmployeeSerializer(employee_query, many=True)
    return Response(serializer.data)
    
@api_view(["GET"])
def employee_detail(request, pk):
    division_query = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(division_query, many=False)
    return Response(serializer.data)
    
@api_view(["POST"])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(["PUT"])
def update_employee(request, pk):
    employee_query = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=employee_query, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(["DELETE"])
def delete_employee(request, pk):
    division_query = Division.objects.get(id=pk)
    division_query.delete()
    content = {"status":"Data Has been deleted"}
    return Response(content, status=status.HTTP_200_OK)
        
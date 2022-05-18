import json
from django.shortcuts import render
from crud.models import Division, Employee
from crud.serializers import DivisionListandDetailSerializer, EmployeeCreatedSerializer, EmployeeSerializer, DivisionCreatedSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework.settings import api_settings


#Endpoint to get division list
@api_view(["GET"])
def divisionList(request):
    division_query = Division.objects.all().order_by("id")
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    paginator = pagination_class()
    page = paginator.paginate_queryset(division_query, request)
    _serializer = DivisionListandDetailSerializer(page, many=True)

    return paginator.get_paginated_response(_serializer.data)


#Endpoint to get division detail
@api_view(["GET"])
def division_detail(request, pk):
    try:
        division_query = Division.objects.get(id=pk)
    except Division.DoesNotExist:
        return Response({"statusCode": status.HTTP_404_NOT_FOUND,"result":"Data Not Found"})
    _serializer = DivisionListandDetailSerializer(division_query, many=False)
    return Response({"statusCode":status.HTTP_200_OK,"result":_serializer.data})
    

#endpoint to create new division
@api_view(["POST"])
def create_division(request):
    serializer = DivisionCreatedSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#endpoint to update existing division 
@api_view(["PUT"])
def update_division(request, pk):
    division_query = Division.objects.get(id=pk)
    serializer = DivisionCreatedSerializer(instance=division_query, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

#endpoint to delete exising division
@api_view(["DELETE"])
def delete_division(request, pk):
    division_query = Division.objects.get(id=pk)
    division_query.delete()
    content = {"status":"Data Has been deleted"}
    return Response(content, status=status.HTTP_200_OK)
        

#endpoint to get employee list
@api_view(["GET"])
def employee_list(request):
    employee_query = Employee.objects.all().order_by("id")
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    paginator = pagination_class()
    page = paginator.paginate_queryset(employee_query, request)
    serializer = EmployeeSerializer(employee_query, many=True)
    return paginator.get_paginated_response(serializer.data)

#endpoint to get employee detail  
@api_view(["GET"])
def employee_detail(request, pk):
    try:
        division_query = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        return Response({"statusCode": status.HTTP_404_NOT_FOUND, "result":"Data Not Found"})
    _serializer = EmployeeSerializer(division_query, many=False)
    return Response({"statusCode":status.HTTP_200_OK,"result":_serializer.data})

#endpoint to create new employee
@api_view(["POST"])
def create_employee(request):
    _serializer = EmployeeCreatedSerializer(data=request.data)
    if _serializer.is_valid():
        _serializer.save()
        return Response({"statusCode":status.HTTP_400_BAD_REQUEST,"status":"Data Has been Submitted","result":_serializer.data})
    else:
        return Response({"statusCode":status.HTTP_400_BAD_REQUEST,"status":"Data Failed to Submitted"})
    

#endpoint to update existing employee
@api_view(["PUT"])
def update_employee(request, pk):
    employee_query = Employee.objects.get(id=pk)
    serializer = EmployeeCreatedSerializer(instance=employee_query, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"statusCode":status.HTTP_202_ACCEPTED,"status":"Data has been Updated"})
    else:
        return Response({"statusCode":status.HTTP_400_BAD_REQUEST,"status":"Data Failed to Updated"})

#endpoint to delete exising employee
@api_view(["DELETE"])
def delete_employee(request, pk):
    try:
        division_query = Employee.objects.get(id=pk).delete()
        content = {"status":"Data Has been deleted"}
        return Response({"statusCode":status.HTTP_202_ACCEPTED,"status":"Data has been Updated"})
    except Employee.DoesNotExist:
        return Response({"statusCode":status.HTTP_400_BAD_REQUEST,"status":"Data Failed to Updated"})
        
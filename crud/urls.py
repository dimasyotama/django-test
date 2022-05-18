from django.urls import path
from crud import views



urlpatterns = [

    #Division URL
    path('create-division/', views.create_division, name="create-division"),
    path('division-list/', views.divisionList, name="division-list"),
    path('division-detail/<int:pk>', views.division_detail, name="division-detail"),
    path('division-delete/<int:pk>', views.delete_division, name="division-delete"),
    path("division-update/<int:pk>", views.update_division, name="division-update"),

    #Employee URL
    path('create-employee/', views.create_employee, name="create-employee"),
    path('employee-list/', views.employee_list, name="employee-list"),
    path('employee-detail/<int:pk>', views.employee_detail, name="employee-detail"),
    path('employee-delete/<int:pk>', views.delete_employee, name="employee-delete"),

]

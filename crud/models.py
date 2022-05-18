from django.db import models

# Create your models here.


class Division(models.Model):
    division_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.division_name


class Employee(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    hire_date = models.DateField(null=True, blank=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self) -> str:
        fullname = self.first_name + self.last_name
        return fullname
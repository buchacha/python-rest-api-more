from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
import json
from .models import Employee, Employer, HR
from .serializers import EmployeeSerializer, EmployerSerializer, HrSerializer

class EmployeesApi(APIView):
    def get(self, request, format=None):
        currents = Employee.objects.all()
        serializer = EmployeeSerializer(currents, many=True)
        return Response({"employees": serializer.data})

    def post(self, request, format=None):
        names = []
        currents = request.data.get('employees')
        for current in currents:
            serializer = EmployeeSerializer(data=current)
            if serializer.is_valid(raise_exception=True):
                currentSaved = serializer.save()
                names.append(currentSaved.name)
        return Response({"success": "Employees '{}' created successfully".format(names)})
        
class EmployersApi(APIView):
    def get(self, request, format=None):
        currents = Employer.objects.all()
        serializer = EmployerSerializer(currents, many=True)
        return Response({"employers": serializer.data})
    def post(self, request, format=None):
        names = []
        currents = request.data.get('employers')
        for current in currents:
            serializer = EmployerSerializer(data=current)
            if serializer.is_valid(raise_exception=True):
                currentSaved = serializer.save()
                names.append(currentSaved.name)
        return Response({"success": "Employers '{}' created successfully".format(names)})

class HRsApi(APIView):
    def get(self, request, format=None):
        currents = HR.objects.all()
        serializer = HrSerializer(currents, many=True)
        return Response({"hrs": serializer.data})
    def post(self, request, format=None):
        names = []
        currents = request.data.get('hrs')
        for current in currents:
            serializer = HrSerializer(data=current)
            if serializer.is_valid(raise_exception=True):
                currentSaved = serializer.save()
                names.append(currentSaved.name)
        return Response({"success": "HRs '{}' created successfully".format(names)})

class EmployeeApi(APIView):
    def get(self, request, employee_pk,format=None):
        current = get_object_or_404(Employee.objects.all(), pk=employee_pk)
        serializer = EmployeeSerializer(current)
        return Response({"employee": serializer.data})
    def delete(self, request, employee_pk, format=None):
        current = get_object_or_404(Employee.objects.all(), pk=employee_pk)
        current.delete()
        return Response({"message": "Employee with id `{}` has been deleted.".format(employee_pk)}, status=204)
    def put(self, request, employee_pk, format=None):
        current = get_object_or_404(Employee.objects.all(), pk=employee_pk)
        data = request.data.get('employee')
        serializer = EmployeeSerializer(instance=current, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            current = serializer.save()
        return Response({
            "success": "Employee '{}' updated successfully".format(current.name)
        })

class EmployerApi(APIView):
    def get(self, request, employer_pk, format=None):
        current = get_object_or_404(Employer.objects.all(), pk=employer_pk)
        serializer = EmployerSerializer(current)
        return Response({"employer": serializer.data})
    def delete(self, request, employer_pk, format=None):
        current = get_object_or_404(Employer.objects.all(), pk=employer_pk)
        current.delete()
        return Response({"message": "Employer with id `{}` has been deleted.".format(employer_pk)}, status=204)
    def put(self, request, employer_pk, format=None):
        current = get_object_or_404(Employer.objects.all(), pk=employer_pk)
        data = request.data.get('employer')
        serializer = EmployerSerializer(instance=current, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            current = serializer.save()
        return Response({
            "success": "Employer '{}' updated successfully".format(current.name)
        })

class HRApi(APIView):
    def get(self, request, hr_pk, format=None):
        current = get_object_or_404(HR.objects.all(), pk=hr_pk)
        serializer = HrSerializer(current)
        return Response({"hr": serializer.data})
    def delete(self, request, hr_pk, format=None):
        current = get_object_or_404(HR.objects.all(), pk=hr_pk)
        current.delete()
        return Response({"message": "HR with id `{}` has been deleted.".format(hr_pk)}, status=204)
    def put(self, request, hr_pk, format=None):
        current = get_object_or_404(HR.objects.all(), pk=hr_pk)
        data = request.data.get('hr')
        serializer = HrSerializer(instance=current, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            current = serializer.save()
        return Response({
            "success": "HR '{}' updated successfully".format(current.name)
        })



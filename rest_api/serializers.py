from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Employee, Employer, HR

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    company = serializers.CharField(max_length=50)
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance

class EmployerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    company = serializers.CharField(max_length=50)
    def create(self, validated_data):
        return Employer.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance

class HrSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    company = serializers.CharField(max_length=50)
    rating = serializers.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(1)])
    def create(self, validated_data):
        return HR.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.company = validated_data.get('company', instance.company)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance


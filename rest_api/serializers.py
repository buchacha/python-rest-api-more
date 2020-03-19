from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Employee, Employer, HR, Skill, Resume, Offer, Position, Rate

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, allow_null=True)
    age = serializers.DateField(allow_null=True)
    city = serializers.CharField(max_length=50, allow_null=True)
    bio = serializers.CharField(allow_null=True)
    photo = serializers.ImageField(allow_null=True, required=False)
    company = serializers.CharField(max_length=50, allow_null=True)
    position = serializers.ChoiceField(choices=Position.choices)
    # resume = serializers.ForeignKey(Resume, allow_null=True)
    skill = serializers.ChoiceField(choices=Skill.choices)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.company = validated_data.get('company', instance.company)
        instance.position = validated_data.get('position', instance.position)
        instance.resume = validated_data.get('resume', instance.resume)
        instance.skill = validated_data.get('skill', instance.skill)

        instance.save()
        return instance

class EmployerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, allow_null=True)
    age = serializers.DateField(allow_null=True)
    city = serializers.CharField(max_length=50, allow_null=True)
    bio = serializers.CharField(allow_null=True)
    photo = serializers.ImageField(allow_null=True, required=False)
    company = serializers.CharField(max_length=50)
    # offer = serializers.ForeignKey(Offer, allow_null=True)

    def create(self, validated_data):
        return Employer.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.company = validated_data.get('company', instance.company)
        instance.offer = validated_data.get('offer', instance.offer)

        instance.save()
        return instance

class HrSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, allow_null=True)
    age = serializers.DateField(allow_null=True)
    city = serializers.CharField(max_length=50, allow_null=True)
    bio = serializers.CharField(allow_null=True)
    photo = serializers.ImageField(allow_null=True, required=False)
    rating = serializers.ChoiceField(
        choices=Rate.choices, 
        allow_null=True
        )
    nsd = serializers.IntegerField(validators=[MinValueValidator(0)])
    # interview = serializers.ForeignKey(Interview, allow_null=True)

    def create(self, validated_data):
        return HR.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.nsd = validated_data.get('nsd', instance.nsd)
        instance.interview = validated_data.get('interview', instance.interview)
        
        instance.save()
        return instance


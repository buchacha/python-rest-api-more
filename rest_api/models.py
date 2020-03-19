from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

class Skill(models.TextChoices):
    CPlusPlus = 'c++'
    C = 'c'
    Java = 'java'
    Python = 'python'
    Backend = 'backend'
    Frontend = 'frontend'
    SQL = 'sql'
    Git = 'git'
    Django = 'django'
    Android = 'android'
    Ios = 'ios'
    Nothing = 'nothing'

class Position(models.TextChoices):
    Intern = 'intern'
    Junior = 'junior'
    Middle = 'middle'
    Senior = 'senior'
    Fullstack = 'fullstack'

class Rate(models.IntegerChoices):
        AAA = 1
        AA = 2
        A = 3
        BBB = 4
        BB = 5
        B = 6 

class Resume(models.Model):
        
    skill = models.CharField(choices=Skill.choices, max_length=50, default='nothing')
    position = models.CharField(choices=Position.choices, max_length=50, default='intern')

class Employee(models.Model):

    name = models.CharField(max_length=50, null=True)
    age = models.DateField(null=True)
    city = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    photo = models.ImageField(upload_to='images/', null=True)
    company = models.CharField(max_length=50, null=True)
    position = models.CharField(choices=Position.choices, max_length=50, default='intern')
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True)
    skill = models.CharField(choices=Skill.choices, max_length=50, default='nothing')

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
 
    def __str__(self):
        return self.name

class Interview(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True)

class HR(models.Model):

    name = models.CharField(max_length=50, null=True)
    age = models.DateField(null=True)
    city = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    photo = models.ImageField(upload_to='images/', null=True)
    rating = models.IntegerField(
        choices=Rate.choices, 
        validators=[MaxValueValidator(6), MinValueValidator(1)],
        null=True
        )
    nsd = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    interview = models.ForeignKey(Interview, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "HR"
        verbose_name_plural = "HRs"
 
    def __str__(self):
        return self.name

class Offer(models.Model):
    skill = models.CharField(choices=Skill.choices, max_length=50, default='nothing')
    position = models.CharField(choices=Position.choices, max_length=50, default='intern')
    salary = models.DecimalField(validators=[MinValueValidator(Decimal('0.01'))], decimal_places=5, max_digits=5, default=Decimal('0.01'))

class Employer(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.DateField(null=True)
    city = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    photo = models.ImageField(upload_to='images/', null=True)
    company = models.CharField(max_length=50)
    offer = models.ForeignKey(Offer, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Employer"
        verbose_name_plural = "Employers"
 
    def __str__(self):
        return self.name
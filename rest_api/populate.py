from .models import Employee, Employer, HR
import random

names = ['Ann', 'Bob', 'Clara', 'Sammy', 'Igor', 'Maria', 'Tommy']
companies = ['Google', 'Yandex', 'Ikea', 'PM-PU', 'Sberbank', 'Huawei', 'Tesla']

for i in range(15):
    employee = Employee()
    employee.name = random.choice(names)
    employee.company = random.choice(companies)
    employee.save()

    employer = Employer()
    employer.name = random.choice(names)
    employer.company = random.choice(companies)
    employer.save()

    hr = HR()
    hr.name = random.choice(names)
    hr.company = random.choice(companies)
    hr.rating = random.choice(range(1,7))
    hr.save()
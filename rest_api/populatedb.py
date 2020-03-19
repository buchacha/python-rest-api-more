from .models import Employer, Employee, HR, Position, Skill
import random
import os
from django.core.files import File
from python_rest_api_hard.settings import STATICFILES_DIRS
from datetime import date


IMG_DIR = os.path.join(STATICFILES_DIRS[0], 'images')
names = ['Taylor', 'Jess', 'Kim', 'Robin', 'Darcy', 'Kris', 'Lou', 'Nicky']
companies = ['Google', 'Yandex', 'Ikea', 'GM', 'Sberbank', 'Huawei', 'Tesla']
img_names = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
bios = [
    'English film director and producer. He is one of the most influential and extensively studied filmmakers in the history of cinema',
    'Born to a poor family in Gori in the Russian Empire (now Georgia), I joined the Marxist Russian Social Democratic Labour Party as a youth',
    'Revealed to be Joseph D. Pistone, an undercover FBI agent. His wife hates his job, and the couple have heated arguments throughout the film'
]
dates = [date(1997, 10, 19), date(1995, 11, 29), date(1980, 2, 19), date(2003, 4, 6), date(1993, 8, 21)]
cities = ['Moscow', 'New-York', 'Los-Angeles', 'Saint-Petersburg', 'Tokio', 'Beijin', 'Kiev']
positions = [x for x in Position]
skills = [x for x in Skill]
nsds = range(0, 22)

def saveImage(current):
    imgName = random.choice(img_names)
    imgPath = os.path.join(IMG_DIR, imgName)
    with open(imgPath, 'rb') as f:   # use 'rb' mode for python3
        data = File(f)
        current.photo.save(imgName, data, True)

def populate():
    # Employee.objects.all().delete()
    # Employer.objects.all().delete()
    # HR.objects.all().delete()

    for i in range(1):
        employee = Employee()
        employee.name = random.choice(names)
        employee.age = random.choice(dates)
        employee.city = random.choice(cities)
        employee.bio = random.choice(bios)
        saveImage(employee)
        employee.company = random.choice(companies)
        employee.position = random.choice(positions)
        employee.skill = random.choice(skills)
        employee.save()

        employer = Employer()
        employer.name = random.choice(names)
        employer.age = random.choice(dates)
        employer.city = random.choice(cities)
        employer.bio = random.choice(bios)
        saveImage(employer)
        employer.company = random.choice(companies)
        employer.save()

        hr = HR()
        hr.name = random.choice(names)
        hr.age = random.choice(dates)
        hr.city = random.choice(cities)
        hr.bio = random.choice(bios)
        saveImage(hr)
        hr.rating = random.choice(range(1,7)) 
        hr.nsd = random.choice(range(0,30))
        saveImage(hr)
        hr.save()
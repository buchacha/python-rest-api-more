from django.urls import path, include
from .views import EmployeesApi, EmployersApi, HRsApi
from .views import EmployeeApi, EmployerApi, HRApi
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='WorkIT API')

urlpatterns = [
    path('docs/', schema_view),
    path('employees/', EmployeesApi.as_view()),
    path('employers/', EmployersApi.as_view()),
    path('hrs/', HRsApi.as_view()),
    path('employee/<int:employee_pk>', EmployeeApi.as_view()),
    path('employer/<int:employer_pk>', EmployerApi.as_view()),
    path('hr/<int:hr_pk>', HRApi.as_view()),
]
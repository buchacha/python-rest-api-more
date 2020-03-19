from django.contrib import admin
from .models import Employee, Employer, HR
from .models import Resume, Offer, Interview


admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(HR)
admin.site.register(Resume)
admin.site.register(Offer)
admin.site.register(Interview)




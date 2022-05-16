from django.contrib import admin

from app_equipments.models import hospital_department
from .models import hospital_department,add_equipment
admin.site.register(hospital_department)
admin.site.register(add_equipment)

# Register your models here.

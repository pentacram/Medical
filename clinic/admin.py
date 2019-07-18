from django.contrib import admin
from .models import *

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinic_name', 'email', 'phone', 'info', 'photo')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'clinic_id', 'name')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'name', 'surname', 'age', 'email', 'phone', 'carrier', 'picture')


    
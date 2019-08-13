from django.contrib import admin
from .models import *


@admin.register(Free_category)
class FreeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(FreeDoctor)
class FreeDoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'catname', 'name', 'surname', 'email', 'phone', 'age', 'info', 'picture')

@admin.register(FreeReserve)
class FreeReserveAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'name', 'surname', 'age', 'date', 'timeslot', 'comment', 'contact_number')


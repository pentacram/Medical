from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import *




class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['clinic_name', 'email', 'phone', 'info', 'photo']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'surname', 'age', 'email', 'phone', 'carrier', 'picture']


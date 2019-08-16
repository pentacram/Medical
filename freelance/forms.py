from django import forms
from django.contrib.auth.models import User
from .models import *


class Free_categoryForm(forms.ModelForm):
    class Meta:
        model = Free_category
        fields = ['name']

class FreeDoctorForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'catname', 'username', 'surname', 'email', 'phone', 'age', 'info', 'picture']

class FreeReserveForm(forms.ModelForm):
    class Meta:
        model = FreeReserve
        fields = ['name', 'surname','comment', 'date', 'timeslot', 'contact_number']
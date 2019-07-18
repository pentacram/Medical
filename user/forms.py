from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput())


    class Meta:
        model = Profile
        fields = ['user', 'firstname', 'lastname', 'email', 'phone', 'images']
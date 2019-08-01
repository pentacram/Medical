from django.forms import ModelForm
from .models import Register
from django.contrib.auth.forms import UserCreationForm


class RegisterCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Register
        fields = ('ad', 'soyad', 'yaş', 'Email', 'əlaqə_nömrəsi') + \
            UserCreationForm.Meta.fields
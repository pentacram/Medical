from django.forms import ModelForm
from .models import Qeydiyyat
from django.contrib.auth.forms import UserCreationForm


class RegisterCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Qeydiyyat
        fields = ('yash', 'elaqe_nomresi') + \
            UserCreationForm.Meta.fields
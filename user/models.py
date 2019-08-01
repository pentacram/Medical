from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


class Register(User):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    yaş = models.PositiveIntegerField()
    Email = models.EmailField(max_length=100, unique=True)
    əlaqə_nömrəsi = PhoneField()

    def __str__(self):
        return f"{self.ad} | {self.soyad} | {self.əlaqə_nömrəsi}"



from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneFormField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    images = models.ImageField(
        upload_to = 'user/images',
        default = 'no-img.jpg',
        blank = True
    )
    firstname = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    email = models.EmailField()
    phone = PhoneFormField()

    def __str__(self):
        return f"{self.user}, {self.firstname}, {self.lastname},{self.email}, {self.phone}, {self.images}"


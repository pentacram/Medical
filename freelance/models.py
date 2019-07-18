from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

class Free_category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name}"

class FreeDoctor(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    catname = models.OneToOneField(Free_category, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    phone = PhoneField()
    age = models.IntegerField()
    info = models.TextField()
    picture = models.ImageField( upload_to = "post1/",
                                 null = True, blank = True )

    def __str__(self):
        return f"{self.username}, {self.catname}, {self.name}, {self.surname}, {self.email}, {self.phone}, {self.age}, {self.info}, {self.picture}"
        
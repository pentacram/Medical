from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

class Clinic(models.Model):
    clinic_name = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    email = models.EmailField(unique=True)
    phone = PhoneField(help_text='Contact phone number', unique=True)
    info = models.TextField()
    photo = models.ImageField(
        upload_to = 'media/clinic/images',
        default = 'no-img.jpg',
        blank=True
    )

    def __str__(self):
        return f"{self.clinic_name}, {self.email}, {self.phone}, {self.info}, {self.photo}"

class Category(models.Model):
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    name = models.CharField(max_length = 55)

    def __str__(self):
        return f"{self.clinic_id}, {self.name}"



class Doctor(models.Model):
    category_id = models.ForeignKey( Category, on_delete = models.CASCADE)
    name = models.CharField( max_length = 50 )
    surname = models.CharField( max_length = 50 )
    age = models.IntegerField( default = None )
    email = models.EmailField(unique=True)
    phone = PhoneField(help_text='Contact phone number', unique=True)
    carrier = models.TextField()
    picture = models.ImageField( upload_to = "post/", null = True, blank = True)
    
    def __str__(self):
        return f"{self.category_id}, {self.name}, {self.surname}, {self.age}, {self.email}, {self.phone}, {self.carrier}, {self.picture}"


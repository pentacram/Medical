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
    picture = models.ImageField( upload_to = "post1/", null = True, blank = True )

    def __str__(self):
        return f"{self.username}, {self.catname}, {self.name}, {self.surname}, {self.email}, {self.phone}, {self.age}, {self.info}, {self.picture}"

class FreeReserve( models.Model ):

    TIMESLOT_LIST = (
        (0, '09:00 – 10:00'),
        (1, '10:00 – 11:00'),
        (2, '11:00 – 12:00'),
        (3, '12:00 – 13:00'),
        (4, '13:00 – 14:00'),
        (5, '14:00 – 15:00'),
        (6, '15:00 – 16:00'),
        (7, '16:00 – 17:00'),
        (8, '17:00 – 18:00'),
    )

    doctor = models.ForeignKey(FreeDoctor, on_delete = models.CASCADE )
    name = models.CharField( max_length = 50 )
    surname = models.CharField( max_length = 50 )
    age = models.IntegerField( default = None )
    date = models.DateField()
    timeslot = models.IntegerField( choices = TIMESLOT_LIST )
    contact_number = models.CharField( max_length = 15 )
    comment = models.CharField( max_length = 1000 )

    def __str__(self):
        return f"{self.name}, {self.doctor}, {self.surname}, {self.age}, {self.date}, {self.timeslot}, {self.comment}"
        
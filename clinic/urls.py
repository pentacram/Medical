from django.urls import path
from .views import *

app_name = "clinic"

urlpatterns = [
    path('', homepage, name = 'homeclinic'),
    path('login/', logins_view, name = 'logins'),
    path('logout/', logout_view, name='logout'),
    path('clinic/<int:id>/update', updateClinic, name='update'),
    path('clinic/<int:id>/category', category, name='category'),
    path('category/<int:id>/doctor', doctor_view, name='doctor'),
    path('category/<int:id>/edit', categoryEdit, name='edit'),
    path('category/<int:id>/delete', categoryDelete, name='delete'),
    path('category/doctors', doctorAllView, name='doctors')
]

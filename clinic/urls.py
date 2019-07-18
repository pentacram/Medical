from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name = 'clinic'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name='logout'),
    path('clinic/<int:id>/update', updateClinic, name='update'),
    path('clinic/<int:id>/category', category, name='category'),
    path('category/<int:id>/doctor', doctor_view, name='doctor'),
    path('category/<int:id>/edit', categoryEdit, name='edit'),
    path('category/<int:id>/delete', categoryDelete, name='delete'),
    path('category/doctors', doctorAllView, name='doctors')
]

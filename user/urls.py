from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('registration', registration, name = 'register'),
    path('logout', logout_view, name = 'logout'),
    path('', freecategory, name = 'home'),
    path('freecategory/<int:id>/freedoctor', freedoctor, name = 'freedoctor'),
    path('freedoctor/<int:id>/freereserve', freereserve, name = 'freereserve'), 
    path('clinic', medicalsview, name = 'clinics'),
    path('clinics/<int:id>', medicalview, name = 'clinic'),
    path('doctor-ajax/', FilterDoctorsAjaxView.as_view(), name = 'doctor-ajax'),
    path('clinic/<int:id>/category', categoryview, name = 'category'),

]
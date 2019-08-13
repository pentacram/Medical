from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name = 'home'),
    path('login/', login_view, name = 'login'),
    path('registration', registration, name = 'register'),
    path('logout', logout_view, name = 'logout'),
    path('freecategory/', freecategory, name = 'freecategory'),
    path('freecategory/<int:id>/freedoctor', freedoctor, name = 'freedoctor'),
    path('freedoctor/<int:id>/freereserve', freereserve, name = 'freereserve'), 
    path('clinic', medicalview, name = 'clinic'),
]
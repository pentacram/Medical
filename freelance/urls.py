from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('login/', login_view, name='login'),
    path('update/', updateDoctor, name='update'),
    path('logout/', logout_view, name='logout')
]
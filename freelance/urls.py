from django.urls import path
from .views import *

app_name = 'freelance'

urlpatterns = [
    path('', homepage, name = 'homefree'),
    path('login/', login_view, name='login'),
    path('update/', updateDoctor, name='update'),
    path('logout/', logout_view, name='logout')
]
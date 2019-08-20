from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def login_view(request):
    if request.User.is_authenticated:
        return redirect('freelance:homepage')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, User)
            return redirect('freelance:homepage')

    return render(request, 'login.html')

@login_required(login_url=reverse_lazy('freelance:login'))
def homepage(request):
    context = {}
    context['doctor'] = FreeDoctor.objects.filter(username__pk = request.user.pk)
    return render(request, 'index.html', context)

@login_required(login_url=reverse_lazy('freelance:login'))
def updateDoctor(request, id):
    context = {}
    profil = FreeDoctor.objects.filter(id = id)
    form = FreeDoctorForm(requet.POST or None, instance=profil)
    context['doctorform'] = profil
    if form.is_valid():
        form.save()
        return redirect('freelance:homepage')
    return render(request, 'doctor-form.html', context)

@login_required(login_url=reverse_lazy('freelance:login'))
def logout_view(request):
    logout(request)
    return redirect('freelance:login')
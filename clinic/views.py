from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def logins_view(request):
    if request.user.is_authenticated:
        return redirect('clinic:homepage')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('clinic:homeclinic')

    return render(request, 'login.html')

@login_required(login_url=reverse_lazy('clinic:logins'))
def homepage(request):
    context ={}
    context['clinic'] = request.user.clinic
    print(context)
    return render(request, 'clinicindex.html', context)

@login_required(login_url=reverse_lazy('clinic:logins'))
def updateClinic(request):
    context = {}
    clinic = Clinic.objects.all()
    form = ClinicForm(request.POST or None, instance=clinic)
    context['clinic'] = clinic
    if form.is_valid():
        form.save()
        return redirect('clinic:homepage')
    return render(request, 'clinic-form', context)

@login_required(login_url=reverse_lazy('clinic:logins'))
def category(request, id):
    context = {}
    context['category'] = Category.objects.filter(clinic_id__pk=id)
    return render(request, 'category.html', context)

@login_required(login_url=reverse_lazy('clinic:logins'))
def categoryEdit(request, id):
    context = {}
    categorys = Clinic.objects.get(id = id)
    form = CategoryForm(request.POST or None, instance=categorys)
    context['categoryform'] = categorys
    if form.is_valid():
        form.save()
        return redirect('clinic:category')
    return render(request, 'category-form.html', context)

@login_required(login_url=reverse_lazy('clinic:logins'))
def categoryDelete(request, id):
    category = Category.objects.get(id=id)

    if request.method == 'GET':
        category.delete()
        return render('clinic:category')

@login_required(login_url=reverse_lazy('clinic:logins'))
def doctor_view(request, id):
    context = {}
    context['doctor'] = Category.objects.filter(id=id)
    return render(request, 'doctors.html', context)


@login_required(login_url=reverse_lazy('clinic:logins'))
def doctorAllView():
    context = {}
    context['doctors'] = Doctor.objects.all()
    return render(request, 'doctors.html', context)




@login_required(login_url=reverse_lazy('clinic:logins'))
def logout_view(request):
    logout(request)
    return redirect('clinic:login')






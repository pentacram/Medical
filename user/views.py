from django.shortcuts import render, redirect
from django.http import Http404
from .models import Register
from .forms import RegisterCreateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from clinic.models import *
from clinic.forms import ReserveForm
from freelance.models import *
from freelance.forms import FreeReserveForm
from django.views.generic import View

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def registration(request):
    if request.method == "POST":
        form = RegisterCreateForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['username'] = request.POST.get('username')
            return redirect('login')
        else:
            return render(request, 'registration.html', context={
                'registration_form': form
            })
    context = {
        'registration_form': RegisterCreateForm()
    }
    return render(request, 'registration.html', context)




def medicalview(request):
    context = {}
    context['medical'] = Clinic.objects.all()
    return render(request, 'klinikalar.html', context)

def categoryview(request, id):
    context = {}
    try:
        context['category'] = Category.objects.filter(clinic_id__pk=id)
    except Category.DoesNotExist:
        raise Http404
    return render(request, 'clinics.html', context)

def doctorview(request, id):
    context = {}
    context['doctor'] = Doctor.objects.filter(category_id__pk=id)
    return render(request, 'doctorview.html', context)

@login_required(login_url=reverse_lazy('login'))
def createreserve(request, id):
    context = {}
    form = ReserveForm(request.POST or None)
    date = request.POST.get('date')
    timeslot = request.POST.get('timeslot')
    if Reserve.objects.filter(date=date, timeslot=timeslot):
        return redirect('createreserve')
    elif form.is_valid():
        form.save()
        return redirect('homepage')
    context['form'] = form
    return render(request, 'reserve.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def freecategory(request):
    context = {}
    context['freecat'] = Free_category.objects.all()
    return render(request, 'index.html', context)

def freedoctor(request, id):
    context = {}
    context['freecat'] = Free_category.objects.all()
    context['freedoctor'] = FreeDoctor.objects.filter(catname__pk=id)
    return render(request, 'freedoc.html', context)


#@login_required(login_url=reverse_lazy('login'))
def freereserve(request, id):
    context = {}
    form = FreeReserveForm(request.POST or None)
    date = request.POST.get('data')
    timeslot = request.POST.get('timeslot')
    if FreeReserve.objects.filter(date=date, timeslot=timeslot):
        return redirect('freereserve')
    elif form.is_valid():
        form.save()
        return redirect('homepage')
    context['freedoctor'] = FreeReserve.objects.filter(doctor__pk=id)
    context['form'] = form
    return render(request, 'freedoc.html', context)


class FilterDoctorsAjaxView(View):
    ajax_template = 'ajax.html'

    def get(self,request):
        if request.is_ajax():
            doctor_type = request.GET.get('doctor_type',False)
            if doctor_type:
                doctors_list = FreeDoctor.objects.filter(catname__name=doctor_type)
                return render(request,self.ajax_template,{'doctors':doctors_list})
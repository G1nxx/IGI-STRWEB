from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from . import models

def index(request):
    # context = {
    #     'services': Service.objects.all(),
    #     'promocodes': PromoCode.objects.all() if not request.user.is_authenticated else None
    # }
    return render(request, 'auto_car/index.html')

def login(request):
    return render(request, 'auto_car/auth/login.html')

@login_required
def logout(request):
    return render(request, 'auto_car/auth/logout.html')

def signup(request):
    return render(request, 'auto_car/auth/signup.html')

@login_required
def client_dashboard(request):
    context = {
        'cars': models.Car.objects.filter(owners=request.user),
        'payments': models.Bill.objects.filter(user=request.user)
    }
    return render(request, 'auto_car/client_dashboard.html', context)

@user_passes_test(lambda u: u.is_employee)
def employee_dashboard(request):
    context = {
        'all_payments': models.Bill.objects.all(),
        'clients': models.User.objects.filter(is_employee=False)
    }
    return render(request, 'auto_car/employee_dashboard.html', context)
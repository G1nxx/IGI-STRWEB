from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import requests
from django.contrib.auth import logout as auth_logout, login as auth_login
from auto_car.usecase import user as user_usecase, company as company_usecases, car as car_usecases
from django.utils import timezone
from .utils.geoip import get_timezone_by_ip

from . import models

def index(request):
    context = {
        # "cars": company_usecases.get_cars(request.session['id']),
    #     'services': Service.objects.all(),
    #     'promocodes': PromoCode.objects.all() if not request.user.is_authenticated else None
    }
    if 'id' in request.session:
        ses_id = request.session['id']
        context['cars'] = company_usecases.get_cars(ses_id)

    user_ip = request.META.get('REMOTE_ADDR')
    # user_ip = '46.216.248.14'
    # user_ip = '169.150.197.223'
    tz_name = get_timezone_by_ip(user_ip)
    timezone.activate(tz_name)
    
    context['time_zone'] = tz_name
    context['current_time'] = timezone.now()

    return render(request, 'auto_car/index.html', context)

def login(request):
    fact = requests.get("https://catfact.ninja/fact").json()
    
    if request.method == 'POST':
        data = {
            "email": request.POST.get("email", ""),
            "password": request.POST.get("password", "")
        }
        user, err = user_usecase.sign_in(data)
        
        if err is None:
            auth_login(request, user.user)
            request.session["role"] = "user"
            request.session["id"] = user.id
            return redirect('/')
        else:
            return render(request, "auto_car/auth/login.html", {
                "fact": fact,
                "error": err
            })
    
    return render(request, 'auto_car/auth/login.html', {"fact": fact})

def signup(request):
    fact = requests.get("https://official-joke-api.appspot.com/random_joke").json()
    
    if request.method == 'POST':
        data = {
            "email": request.POST.get("email", ""),
            "password": request.POST.get("password", ""),
            "username": request.POST.get("username", ""),
            "phone": request.POST.get("phone", ""),
            "birthday_date": request.POST.get("birthday", "")
        }
        
        user, err = user_usecase.sign_up(data)
        
        if err:
            return render(request, "auto_car/auth/signup.html", {
                "fact": fact,
                "error": err,
                "form_data": data
            })
        
        auth_login(request, user.user)
        if user.is_employee:
            request.session["role"] = "employee"
        else:
            request.session["role"] = "user"
        request.session["id"] = user.id
        return redirect('/') 
    
    return render(request, "auto_car/auth/signup.html", {
        "fact": fact,
        "error": ""
    })

@login_required
def logout(request):
    auth_logout(request)
    
    if 'role' in request.session:
        del request.session['role']
    if 'id' in request.session:
        del request.session['id']
    
    request.session.flush()
    
    return redirect('/')

@login_required
def client_dashboard(request):
    context = {
        'cars': models.Car.objects.filter(owners=user_usecase.get_user(request.user.email)),
        #'payments': models.Bill.objects.filter(user=request.user.em)
    }
    return render(request, 'auto_car/client_dashboard.html', context)

@user_passes_test(lambda u: u.is_staff)
def employee_dashboard(request):
    daily_stats = models.UserSession.get_daily_stats()[:30]
    avg_time = models.UserSession.get_average_session_time()
    context = {
        'all_payments': models.Bill.objects.all(),
        'clients': models.ServiceUser.objects.filter(is_employee=False),
        'daily_stats': daily_stats,
        'avg_time': avg_time,
    }
    return render(request, 'auto_car/employee_dashboard.html', context)

def about(request):
    context = {
        'about': {
            'info': company_usecases.get_info()
            }
        }
    return render(request, 'auto_car/company/about.html', context)

def news(request):
    context = {
        'news': models.News.objects.all()
    }
    return render(request, 'auto_car/company/news.html', context)

def glossary(request):
    return render(request, 'auto_car/company/glossary.html')

def contacts(request):
    return render(request, 'auto_car/company/contacts.html')

def privacy(request):
    return render(request, 'auto_car/company/privacy.html')

def vacancies(request):
    return render(request, 'auto_car/company/vacancies.html')

def reviews(request):
    return render(request, 'auto_car/company/reviews.html')

def promocodes(request):
    return render(request, 'auto_car/company/promocodes.html')

@login_required
def park_car(request, car_id):
    context = {
        'car_id': car_id,
        'parking_places': company_usecases.get_free_parking_places()
    }
    return render(request, 'auto_car/park_car.html', context)

@login_required
def park(request, parking_id, car_id):
    context = {
        'ok': company_usecases.park_car(parking_id, car_id)
    }
    return render(request, 'auto_car/park.html', context)

@login_required
def unpark_car(request, car_id):
    context = {
        'ok': company_usecases.unpark_car(car_id)
    }
    return render(request, 'auto_car/unpark.html', context)

@login_required
def register_car(request):
    context = {
        'user_id': request.session['id'],
    }
    return render(request, 'auto_car/register_car.html', context)

@login_required
def create_car(request, user_id):
    if request.method == 'POST':
        data = {
            "brand": request.POST.get("brand", ""),
            "model": request.POST.get("model", ""),
            "number": request.POST.get("number", ""),
            "type": request.POST.get("type", ""),
            "user_id": user_id,
        }
        context = {
            'ok': car_usecases.create_car(data),
            'type': "create",
        }
        return render(request, 'auto_car/car_crud_info.html', context)
    return render(request, 'auto_car/car_crud_info.html', {'ok': False, 'type': 'create'})

@login_required
def delete_car(request, car_id):
    if request.method == 'POST':
        context = {
            'ok': car_usecases.delete_car(car_id),
            'type': "delete"
        }
        return render(request, 'auto_car/car_crud_info.html', context)
    return render(request, 'auto_car/car_crud_info.html', {'ok': False, 'type': 'delete'})

@login_required
def update_car(request, car_id):
    data = car_usecases.read_car(car_id)
    context = {
        'car_id': car_id,
        'data': data,
    }
    return render(request, 'auto_car/update_car.html', context)

@login_required
def update(request, car_id):
    if request.method == 'POST':
        data = {
            "brand": request.POST.get("brand", "").strip(),
            "model": request.POST.get("model", "").strip(),
            "number": request.POST.get("number", "").strip(),
            "type": request.POST.get("type", "").strip(),
        }
        context = {
            'ok': car_usecases.update_car(car_id, data),
            'type': "update"
        }
        return render(request, 'auto_car/car_crud_info.html', context)
    return render(request, 'auto_car/car_crud_info.html', {'ok': False, 'type': 'update'})
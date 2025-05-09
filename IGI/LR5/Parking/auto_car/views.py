from django.shortcuts import render

def index(request):
    return render(request, 'auto_car/index.html')

def login(request):
    return render(request, 'auto_car/auth/login.html')

def logout(request):
    return render(request, 'auto_car/auth/logout.html')

def signup(request):
    return render(request, 'auto_car/auth/signup.html')

def client_dashboard(request):
    return render(request, 'auto_car/client_dashboard.html')

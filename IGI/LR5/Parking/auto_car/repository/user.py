from auto_car.models import ServiceUser, Car
from django.contrib.auth.models import User

def create_user(data):
    birthday = data.pop('birthday_date', None)
    phone = data.pop('phone', None)
    user = User.objects.create(**data)
    new_data = {"user": user, "birthday_date": birthday, "phone": phone}
    return ServiceUser.objects.create(**new_data)

def get_user_by_username(username):
    try:
        return ServiceUser.objects.get(username=username)
    except ServiceUser.DoesNotExist:
        return None
    
def get_user_by_email(eml):
    try:
        return ServiceUser.objects.get(user__email=eml)
    except ServiceUser.DoesNotExist:
        return None

def get_employees():
    try:
        return ServiceUser.objects.filter(is_employee=True)
    except Exception:
        return []

def get_user_cars(ServiceUser):
    try:
        return ServiceUser.cars_owned.all()
    except Exception:
        return []

def get_cars_by_brand(brand):
    try:
        return Car.objects.filter(brand__iexact=brand)
    except Exception:
        return []

def get_car_by_number(number):
    try:
        return Car.objects.get(number=number)
    except Car.DoesNotExist:
        return None
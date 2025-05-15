from auto_car.models import CompanyInfo, ParkingSpace, Car, News, Review, Contact, Coupon, Vacancy, FAQ
from django.db import transaction

def get_company_info():
    return CompanyInfo.objects.first()

def get_free_parking_places():
    return ParkingSpace.objects.filter(is_free=True)

def get_cars(id):
    return Car.objects.filter(owners__id=id)

def park_car(p_id, c_id):
    try:
        with transaction.atomic():
            car = Car.objects.get(id=c_id)
            parking_space = ParkingSpace.objects.get(number=p_id, is_free=True)
            
            car.is_parked = True
            car.save()
            
            parking_space.is_free = False
            parking_space.parked_car = car
            parking_space.save()
            
            return True
    except (Car.DoesNotExist, ParkingSpace.DoesNotExist):
        return False
    
def unpark_car(c_id):
    try:
        with transaction.atomic():
            car = Car.objects.get(id=c_id)
            parking_space = ParkingSpace.objects.get(parked_car__id=c_id, is_free=False)
            
            car.is_parked = False
            car.save()
            
            parking_space.is_free = True
            parking_space.parked_car = None
            parking_space.save()
            
            return True
    except (Car.DoesNotExist, ParkingSpace.DoesNotExist):
        return False
    
def get_last_news():
    return News.objects.all().last

def get_reviews():
    return Review.objects.all()

def create_review(data):
    return Review.objects.create(**data)

def get_contacts():
    return Contact.objects.all()

def get_promocodes():
    return Coupon.objects.all()

def get_glossaries():
    return FAQ.objects.all()

def get_vacancies():
    return Vacancy.objects.all()
from auto_car.models import CompanyInfo, ParkingSpace, Car
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
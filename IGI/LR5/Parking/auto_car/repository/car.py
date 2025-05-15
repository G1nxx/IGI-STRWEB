from django.shortcuts import get_object_or_404
from auto_car.models import Car, ServiceUser
from django.db import transaction

def create(data):
    if Car.objects.filter(number=data["number"]).exists():
        return None
        
    with transaction.atomic():
        user_id = data.pop('user_id')
        car = Car.objects.create(**data)
        service_user = get_object_or_404(ServiceUser, id=user_id)
        car.owners.add(service_user)
        return car
    return None

def update(car_id, data):
    car = get_object_or_404(Car, id=car_id)
    for field, value in data.items():
        setattr(car, field, value)
    car.save()
    return car

def read(car_id):
    return get_object_or_404(Car, id=car_id)

def delete(car_id):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return True
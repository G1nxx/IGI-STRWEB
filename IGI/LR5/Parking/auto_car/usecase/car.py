from django.contrib.auth.models import User
from auto_car.repository import car as car_db

def create_car(data):
    car = car_db.create(data)
    if car != None:
        return True
    return False

def update_car(car_id, data):
    car = car_db.update(car_id, data)
    if car != None:
        return True
    return False

def read_car(car_id):
    return car_db.read(car_id)

def delete_car(car_id):
    return car_db.delete(car_id)
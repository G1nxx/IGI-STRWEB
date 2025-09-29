from auto_car.models import CompanyInfo, ParkingSpace, Car, Cart, News, Review, Contact, Coupon, Vacancy, FAQ, YearHistory, Service, Partner, ServiceUser, OrderService
from django.db import transaction
from time import timezone

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

def get_year_history():
    return YearHistory.objects.all()

def get_services():
    return Service.objects.all()

def get_partners():
    return Partner.objects.all()

def add_to_cart(u_id, service_id):
    s_usr = ServiceUser.objects.get(user_id=u_id)
    cart = Cart.objects.get(user=s_usr)
    service = Service.objects.get(id=service_id)
    
    o_service, created_os = OrderService.objects.get_or_create(
        service=service,
        defaults={'quantity': 1}
    )
    
    if cart.goods.filter(id=o_service.id).exists():
        o_service.quantity += 1
        o_service.save()
    else:
        cart.goods.add(o_service)
    
    cart.save()

def get_cart(u_id):
    s_usr = ServiceUser.objects.get(user_id=u_id)
    cart = Cart.objects.get(user=s_usr)
    return cart.goods.all()

def update_order(id, val):
    ord = OrderService.objects.get(id=id)
    ord.quantity = val
    ord.save()

def delete_order(id):
    ord = OrderService.objects.get(id=id)
    ord.delete()

def bye_cart(u_id):
    s_usr = ServiceUser.objects.get(user_id=u_id)
    cart = Cart.objects.get(user=s_usr)
    goods = cart.goods.all()
    for g in goods :
        g.delete()
    
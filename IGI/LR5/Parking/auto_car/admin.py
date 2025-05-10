from django.contrib import admin
from auto_car.models import *

admin.site.register(User)
admin.site.register(Car)
admin.site.register(ParkingSpace)
admin.site.register(Bill)
admin.site.register(Income)
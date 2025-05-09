from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='client_groups',
        related_query_name='client',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='client_user_permissions',
        related_query_name='client',
    )

    def __str__(self):
        pass

class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    number = models.CharField(max_length=15)
    type = models.CharField(max_length=10)
    owners = models.ManyToManyField(Client, related_name='cars_owned')
    
    def __str__(self):
        pass

class ParkingSpace(models.Model):
    number = models.CharField(max_length=10, unique=True)
    cost_per_month = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_free = models.BooleanField(default=True)
    type = models.CharField(max_length=20)
    
    def __str__(self):
        pass

class Bill(models.Model):
    code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        pass

class Income(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    bills = models.ManyToManyField(Bill, related_name="bills")
    
    def __str__(self):
        pass
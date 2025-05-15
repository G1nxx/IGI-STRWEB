from django.db import models
from django.db.models import Avg, Count, Max
from django.contrib.auth.models import User
import django.utils.timezone as timezone
from django.db.models.functions import TruncDate
from datetime import timedelta

class ServiceUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    is_employee = models.BooleanField(default=False)
    birthday_date = models.DateField(default=timezone.now)

    def get_full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return self.user.username

class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    number = models.CharField(max_length=15)
    type = models.CharField(max_length=10)
    is_parked = models.BooleanField(default=False)
    owners = models.ManyToManyField(ServiceUser, related_name='cars_owned')
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.number})"

class ParkingSpace(models.Model):
    number = models.CharField(max_length=10, unique=True)
    cost_per_month = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_free = models.BooleanField(default=True)
    type = models.CharField(max_length=20)
    parked_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        status = "Свободно" if self.is_free else "Занято"
        return f"Место {self.number} ({self.type}, {status}, {self.cost_per_month} руб/мес)"

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
        status = "Оплачен" if self.is_paid else "Не оплачен"
        return f"Счет #{self.code} ({self.car} - {self.amount} руб, {status})"

class Income(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    bills = models.ManyToManyField(Bill, related_name="incomes")
    
    def __str__(self):
        return f"Доход за {self.date.strftime('%d.%m.%Y')}: {self.amount} руб ({self.description[:30]}...)"
    
class VacancyInfo(models.Model):
    info = models.TextField()

    def __str__(self):
        return f"Информация о вакансии: {self.info[:50]}..." if len(self.info) > 50 else self.info

class Vacancy(models.Model):    
    name = models.TextField()
    salary = models.FloatField()
    info = models.OneToOneField(VacancyInfo, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Вакансия: {self.name} ({self.salary} руб.)"

class CompanyInfo(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class News(models.Model):
    title = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Новость: {self.title} ({self.date.strftime('%d.%m.%Y')})"

class FAQ(models.Model):
    text = models.TextField()
    answer = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Вопрос: {self.text[:50]}..." if len(self.text) > 50 else self.text

class Review(models.Model):
    customer = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    rate = models.IntegerField()
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.customer.user.username}: {self.rate}★ ({self.date.strftime('%d.%m.%Y')})"

class Coupon(models.Model):
    number = models.IntegerField()
    deadline = models.DateTimeField(auto_now_add=True)
    discount = models.IntegerField()

    def __str__(self):
        return f"Купон #{self.number}: скидка {self.discount}% (до {self.deadline.strftime('%d.%m.%Y')})"
    
class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.logout_time and self.login_time:
            self.duration = self.logout_time - self.login_time
        super().save(*args, **kwargs)
    
    @classmethod
    def get_daily_stats(cls):
        return cls.objects.annotate(
            date=TruncDate('login_time')
        ).values('date').annotate(
            users=Count('user', distinct=True),
            sessions=Count('id'),
            avg_duration=Avg('duration')
        ).order_by('-date')
    
    @classmethod
    def get_user_stats(cls, user):
        return cls.objects.filter(user=user).aggregate(
            total_sessions=Count('id'),
            avg_time=Avg('duration'),
            last_seen=Max('login_time')
        )
    
    @classmethod
    def get_average_session_time(cls):
        return cls.objects.exclude(duration__isnull=True).aggregate(
            avg_duration=Avg('duration')
        )['avg_duration'] or timedelta(0)
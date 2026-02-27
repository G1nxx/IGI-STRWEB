from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import (
    ServiceUser, Car, ParkingSpace, Bill,
    Income, VacancyInfo, Vacancy,
    Review, Coupon, UserSession
)
from datetime import datetime, timedelta
from .usecase.user import sign_up, sign_in, get_user
from unittest.mock import patch

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        
        self.service_user = ServiceUser.objects.create(
            user=self.user,
            phone='+79991234567',
            address='Test Address',
            is_employee=False,
            birthday_date=timezone.now().date()
        )
        
        self.car = Car.objects.create(
            brand='Toyota',
            model='Camry',
            number='A123BC',
            type='Sedan'
        )
        self.car.owners.add(self.service_user)
        
        self.parking_space = ParkingSpace.objects.create(
            number='A01',
            cost_per_month=5000.00,
            is_free=False,
            type='Standard',
            parked_car=self.car
        )
        
        self.bill = Bill.objects.create(
            code='BILL123',
            parking_space=self.parking_space,
            car=self.car,
            amount=5000.00
        )
        
        self.now = timezone.now()

    def test_service_user_creation(self):
        self.assertEqual(self.service_user.get_full_name(), 'Test User')
        self.assertEqual(str(self.service_user), 'testuser')
        self.assertFalse(self.service_user.is_employee)
        
    def test_car_creation(self):
        self.assertEqual(str(self.car), 'Toyota Camry (A123BC)')
        self.assertEqual(self.car.owners.first(), self.service_user)
        self.assertFalse(self.car.is_parked)
        
    def test_parking_space_creation(self):
        self.assertEqual(str(self.parking_space), 
                         'Место A01 (Standard, Занято, 5000.0 руб/мес)')
        self.assertEqual(self.parking_space.parked_car, self.car)
        
    def test_bill_creation(self):
        self.assertEqual(str(self.bill), 
                        'Счет #BILL123 (Toyota Camry (A123BC) - 5000.0 руб, Не оплачен)')
        self.assertFalse(self.bill.is_paid)
        
    def test_bill_payment(self):
        self.bill.paid_amount = 5000.00
        self.bill.is_paid = True
        self.bill.paid_at = timezone.now()
        self.bill.save()
        
        self.assertTrue(self.bill.is_paid)
        self.assertEqual(self.bill.paid_amount, 5000.00)
        
    def test_income_creation(self):
        income = Income.objects.create(
            date=timezone.now().date(),
            amount=10000.00,
            description='Test income'
        )
        income.bills.add(self.bill)
        
        self.assertEqual(income.bills.count(), 1)
        self.assertIn('Test income', str(income))
        
    def test_vacancy_creation(self):
        info = VacancyInfo.objects.create(info='Test vacancy info')
        vacancy = Vacancy.objects.create(
            name='Test Position',
            salary=100000.00,
            info=info
        )
        
        self.assertEqual(str(vacancy), 'Вакансия: Test Position (100000.0 руб.)')
        self.assertEqual(vacancy.info.info, 'Test vacancy info')
        
    def test_user_session_duration(self):
        login_time = self.now - timedelta(hours=1)
        logout_time = self.now
        
        session = UserSession.objects.create(
            user=self.user,
            session_key='testsessionkey',
            login_time=login_time,
            logout_time=logout_time
        )
        
        self.assertEqual(session.duration, timedelta(hours=1))
        
    def test_coupon_expiration(self):
        coupon = Coupon.objects.create(
            number=12345,
            deadline=self.now + timedelta(days=7),
            discount=10
        )
        
        self.assertIn('10%', str(coupon))
        self.assertTrue(coupon.deadline > self.now)
        
    def test_review_rating(self):
        review = Review.objects.create(
            customer=self.service_user,
            rate=5,
            text='Excellent service!'
        )
        
        self.assertEqual(review.rate, 5)
        self.assertIn('5★', str(review))
        
    def test_parking_space_release(self):
        self.parking_space.is_free = True
        self.parking_space.parked_car = None
        self.parking_space.save()
        
        self.assertTrue(self.parking_space.is_free)
        self.assertIsNone(self.parking_space.parked_car)

    def test_car_parking_status(self):
        self.car.is_parked = True
        self.car.save()
        
        self.assertTrue(self.car.is_parked)

class AuthServicesTests(TestCase):
    def setUp(self):
        self.valid_user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass123",
            "phone": "+375291234567",
            "birthday_date": "1990-01-01"
        }
        
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.service_user = ServiceUser.objects.create(
            user=self.user,
            phone="+375291234567"
        )
        
        self.user_db_patcher = patch('auto_car.repository.user')
        self.mock_user_db = self.user_db_patcher.start()
        self.addCleanup(self.user_db_patcher.stop)
    
    def test_sign_up_age_restriction(self):
        young_user_data = self.valid_user_data.copy()
        young_user_data["birthday_date"] = (datetime.now() - timedelta(days=365*17)).strftime("%Y-%m-%d")
        
        user, error = sign_up(young_user_data)
        
        self.assertIsNone(user)
        self.assertEqual(error, "You must be at least 18 years old")

    def test_sign_up_username_validation(self):
        short_name_data = self.valid_user_data.copy()
        short_name_data["username"] = "abc"
        
        user, error = sign_up(short_name_data)
        
        self.assertIsNone(user)
        self.assertEqual(error, "Name must be longer than 5 characters")

    def test_sign_up_phone_validation(self):
        invalid_phone_data = self.valid_user_data.copy()
        invalid_phone_data["phone"] = "+37529123"
        user, error = sign_up(invalid_phone_data)
        self.assertIsNone(user)
        self.assertEqual(error, "Invalid phone number format")
        
        invalid_prefix_data = self.valid_user_data.copy()
        invalid_prefix_data["phone"] = "+123456789012"
        user, error = sign_up(invalid_prefix_data)
        self.assertIsNone(user)
        self.assertEqual(error, "Phone number must start with +37529")

    def test_sign_up_email_validation(self):
        short_email_data = self.valid_user_data.copy()
        short_email_data["email"] = "a@b.c"
        
        user, error = sign_up(short_email_data)
        
        self.assertIsNone(user)
        self.assertEqual(error, "Email must be longer than 7 characters")

    def test_sign_up_password_validation(self):
        short_pass_data = self.valid_user_data.copy()
        short_pass_data["password"] = "12345"
        
        user, error = sign_up(short_pass_data)
        
        self.assertIsNone(user)
        self.assertEqual(error, "Password must be at least 8 characters long")

    def test_sign_up_existing_user(self):
        self.mock_user_db.get_user_by_email.return_value = self.service_user
        
        user, error = sign_up(self.valid_user_data)
        
        self.assertIsNone(user)
        self.assertEqual(error, "User already exists")

    def test_sign_in_wrong_email(self):
        self.mock_user_db.get_user_by_email.return_value = None
        
        user, error = sign_in({
            "email": "wrong@example.com",
            "password": "testpass123"
        })
        
        self.assertIsNone(user)
        self.assertEqual(error, "User not found")

    def test_sign_in_invalid_email_format(self):
        user, error = sign_in({
            "email": "invalid-email",
            "password": "testpass123"
        })
        
        self.assertIsNone(user)
        self.assertEqual(error, "Wrong email")

    def test_sign_in_wrong_password(self):
        self.mock_user_db.get_user_by_email.return_value = self.service_user
        
        user, error = sign_in({
            "email": "test@example.com",
            "password": "wrongpass"
        })
        
        self.assertIsNone(user)
        self.assertEqual(error, "Wrong password")

    def test_sign_in_short_password(self):
        user, error = sign_in({
            "email": "test@example.com",
            "password": "short"
        })
        
        self.assertIsNone(user)
        self.assertEqual(error, "Password must be at least 8 characters long")

    def test_get_user_success(self):
        self.mock_user_db.get_user_by_email.return_value = self.service_user
        
        user = get_user("test@example.com")
        
        self.assertEqual(user, self.service_user)

    def test_get_user_not_found(self):
        self.mock_user_db.get_user_by_email.return_value = None
        
        user = get_user("nonexistent@example.com")
        
        self.assertIsNone(user)
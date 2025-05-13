from django.urls import path
from . import views

app_name = 'auto_car'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('client_dashboard/', views.client_dashboard, name='client_dashboard'),
    path('employee/', views.employee_dashboard, name='employee_dashboard'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('glossary/', views.glossary, name='glossary'),
    path('contacts/', views.contacts, name='contacts'),
    path('privacy/', views.privacy, name='privacy'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('reviews/', views.reviews, name='reviews'),
    path('promocodes/', views.promocodes, name='promocodes'),
    path('client_dashboard/park_car/<int:car_id>/', views.park_car, name='client_dashboard/park_car'),
    path('client_dashboard/park_car/park/<str:parking_id>/<int:car_id>/', views.park, name='client_dashboard/park_car/park'),
]

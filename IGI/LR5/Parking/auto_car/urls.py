from django.urls import path
from . import views

app_name = 'auto_car'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('client_dashboard/', views.client_dashboard, name='client_dashboard')
]
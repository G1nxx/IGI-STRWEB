from django.urls import path, re_path
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
    re_path(r'^client_dashboard/park_car/park/(?P<parking_id>[a-zA-Z0-9_-]+)/(?P<car_id>\d+)/$', views.park, name='client_dashboard/park_car/park'),
    re_path(r'^client_dashboard/unpark_car/(?P<car_id>\d+)/$', views.unpark_car, name='client_dashboard/unpark_car'),
    path('client_dashboard/register_car/', views.register_car, name='client_dashboard/register_car'),
    re_path(r'^client_dashboard/register_car/create_car/(?P<user_id>\d+)/$', views.create_car, name='client_dashboard/register_car/create_car'),
    re_path(r'^client_dashboard/delete_car/(?P<car_id>\d+)/$', views.delete_car, name='client_dashboard/delete_car'),
    re_path(r'^client_dashboard/update_car/(?P<car_id>\d+)/$', views.update_car, name='client_dashboard/update_car'),
    re_path(r'^client_dashboard/update_car/update/(?P<car_id>\d+)/$', views.update, name='client_dashboard/update_car/update'),
]

from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'auto_car'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cart/<int:u_id>/', views.cart, name='cart'),
    path('bye_cart/<int:u_id>/', views.bye_cart, name='bye_cart'),
    path('update_order/<int:u_id>/<int:id>/', views.update_order, name='update_order'),
    path('delete_order/<int:u_id>/<int:id>/', views.delete_order, name='delete_order'),
    path('demonstration/', views.demonstration, name='demonstration'),
    path('add_to_cart/<int:u_id>/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('client_dashboard/', views.client_dashboard, name='client_dashboard'),
    path('employee/', views.employee_dashboard, name='employee_dashboard'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('news/read_more/<int:_id>/<str:type>/', views.read_more, name='news/read_more'),
    # path('reviews/read_more/<int:_id>/<str:type>/', views.read_more, name='review/read_more'),
    path('glossary/', views.glossary, name='glossary'),
    path('contacts/', views.contacts, name='contacts'),
    path('employees/', views.employees_data_json, name='employees_data_json'),
    path('privacy/', views.privacy, name='privacy'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('reviews/', views.reviews, name='reviews'),
    path('add_review/', views.add_review, name='add_review'),
    path('promocodes/', views.promocodes, name='promocodes'),
    path('client_dashboard/park_car/<int:car_id>/', views.park_car, name='client_dashboard/park_car'),
    re_path(r'^client_dashboard/park_car/park/(?P<parking_id>[a-zA-Z0-9_-]+)/(?P<car_id>\d+)/$', views.park, name='client_dashboard/park_car/park'),
    re_path(r'^client_dashboard/unpark_car/(?P<car_id>\d+)/$', views.unpark_car, name='client_dashboard/unpark_car'),
    path('client_dashboard/register_car/', views.register_car, name='client_dashboard/register_car'),
    re_path(r'^client_dashboard/register_car/create_car/(?P<user_id>\d+)/$', views.create_car, name='client_dashboard/register_car/create_car'),
    re_path(r'^client_dashboard/delete_car/(?P<car_id>\d+)/$', views.delete_car, name='client_dashboard/delete_car'),
    re_path(r'^client_dashboard/update_car/(?P<car_id>\d+)/$', views.update_car, name='client_dashboard/update_car'),
    re_path(r'^client_dashboard/update_car/update/(?P<car_id>\d+)/$', views.update, name='client_dashboard/update_car/update'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

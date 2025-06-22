#define URL route for index() view
from django.urls import path
from .views import MenuItemView, SingleMenuItemView
from . import views
from rest_framework.authtoken.views import obtain_auth_token

#add following lines to urlpatterns list 
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('bookings', views.bookings, name='bookings'), 
    path('menu/', views.menu_view, name="menu"),
    path('api-token-auth/', obtain_auth_token),
]


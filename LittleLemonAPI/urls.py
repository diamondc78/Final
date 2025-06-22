from django.urls import path
from .views import MenuItemView, SingleMenuItemView, msg, BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('menu/', menu_view, name='menu'),
    path('menu-items/', MenuItemView.as_view(), name='menu_items'),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name='single_menu_item'),
    path('message/', msg),
    path('api-token-auth/', obtain_auth_token)
    
]
from django.urls import path
from drinkapp import views
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  
    TokenRefreshView,   
)

urlpatterns = [
     path('apilogin/', auth_views.LoginView.as_view(), name='login'),
   

   path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', views.register, name='register'),

    path('customers/', views.manage_Customer, name='manage_customer'),
    path('customers/<int:id>/', views.manage_Customer, name='manage_customer_detail'),

    path('orders/', views.manage_Order, name='manage_order'),
    path('orders/<int:id>/', views.manage_Order, name='manage_order_detail'),

    path('payments/', views.manage_Payment, name='manage_payment'),
    path('payments/<int:id>/', views.manage_Payment, name='manage_payment_detail'),

    path('MotorcycleType/', views.manage_MotorcycleType, name='manage_MotorcycleType'),
    path('MotorcycleType/<int:id>/', views.manage_MotorcycleType, name='MotorcycleType_detail'),
]





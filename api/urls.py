from django.urls import path
from drinkapp import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  
    TokenRefreshView,   
)

urlpatterns = [
path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

path('Customer/',views.manage_Customer),
path('Customer/<int:id>/',views.manage_Customer),

path('Order/',views.manage_Order),
path('Order/<int:id>/',views.manage_Order),

path('Payment/',views.manage_Payment),
path('Payment/<int:id>/',views.manage_Payment),

]
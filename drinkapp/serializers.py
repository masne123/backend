from rest_framework import serializers
from .models  import *

class CustomerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields ='__all__'  


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields ='__all__' 

    
class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields ='__all__' 

    
class MotorcycleTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = MotorcycleType
        fields ='__all__'     
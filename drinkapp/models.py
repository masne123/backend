from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    password = models.CharField(max_length=50, default='defaultpassword')  #

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Order(models.Model):
    order_number = models.CharField(max_length=100)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Dispatched', 'Dispatched'),
            ('In Transit', 'In Transit'),
            ('Delivered', 'Delivered'),
        ],
        default='Pending'
    )

    def __str__(self):
        return f"Order {self.order_number} - {self.status}"


class Payment(models.Model):
    payment_id = models.CharField(max_length=255, unique=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_number = models.CharField(max_length=100)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Completed', 'Completed'),
            ('Failed', 'Failed'),
        ],
        default='Pending'
    )

    def __str__(self):
        return f"Payment {self.payment_id} - {self.status}"


class MotorcycleType(models.Model):
    name = models.CharField(max_length=50, unique=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    description = models.TextField(blank=True, null=True)  
    engine_capacity = models.CharField(max_length=50, blank=True, null=True)  
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  
    fuel_type = models.CharField(max_length=50, blank=True, null=True)  
    max_speed = models.IntegerField(blank=True, null=True)  
    year_of_manufacture = models.IntegerField(blank=True, null=True)  
    features = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.name
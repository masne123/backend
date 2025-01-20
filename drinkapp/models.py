from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,null=True,blank=True)
    phone_number = models.CharField(max_length=15)
    address =models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    def __str__(self):
     return f'{self.first_name} {self.last_name}'
    
    
class Order(models.Model):
 
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    order_id = models.IntegerField()
    # New fields for motorcycle delivery system
    delivery_status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Dispatched', 'Dispatched'),
            ('In Transit', 'In Transit'),
            ('Delivered', 'Delivered'),
        ],
        default='Pending'
    )
    motocycle_type =models.CharField(
        max_length = 50,
        choices=[
        ('toyota Camry', 'Toyota Camry'),
        ('cruiser', 'Cruiser'),
        ('BMW 3', 'BMW 3'),
        ('Nissan Qashqai', 'Nissan Qashqai'),
        ('Mazda CX-5', 'Mazda CX-5'),
        ('Ford Mustang Convertible', 'Ford Mustang Convertible'),
        ('dirtbike', 'Dirtbike'),
        ],
    )
    delivery_time = models.DateTimeField(null=True, blank=True)
    rider_name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f'Order by {self.customer} on {self.created_on.strftime("%b %d %Y %I:%M %p")} - Status: {self.delivery_status}'

    def mark_as_delivered(self):
        self.delivery_status = 'Delivered'
        self.delivery_time = models.DateTimeField(auto_now=True)  # Sets delivery time to now
        self.save()

    def is_delivered(self):
        return self.delivery_status == 'Delivered'
    
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    payment_date = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending') 
    method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer')], default='credit_card')  
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    order_id = models.IntegerField()
    def __str__(self):
        return f"Payment {self.id} - {self.status}"



    
    
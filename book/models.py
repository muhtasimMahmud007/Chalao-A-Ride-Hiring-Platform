from django.db import models

class Booking(models.Model):

    customer_email = models.EmailField(null=True,blank=True)
    pickup_location = models.CharField(max_length=100,null=True,blank=True)
    destination = models.CharField(max_length=100,null=True,blank=True)
    distance = models.CharField(max_length=100,null=True,blank=True)
    pickup_date = models.DateField(null=True,blank=True)
    pickup_time = models.TimeField(null=True,blank=True)
    num_passengers = models.PositiveIntegerField(null=True,blank=True)
    vehicle_type = models.CharField(max_length=50,null=True,blank=True)
    total_amount = models.PositiveIntegerField(default=0,null=True,blank=True)
    is_anonymous=models.BooleanField(default=False,null=True,blank=True)
    is_authenticated=models.BooleanField(default=True,null=True,blank=True)
    USERNAME_FIELD = 'customer_email'
    REQUIRED_FIELDS = ['pickup_location','destination','distance','pickup_date','pickup_time',
    'num_passengers','vehicle_type']
    
    def __str__(self):
        return f"{self.customer_email} : {self.pickup_location}"
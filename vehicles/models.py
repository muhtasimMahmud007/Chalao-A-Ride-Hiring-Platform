from django.db import models

# Create your models here.
class Vehicle(models.Model):
    Vehicle_license_plate = models.CharField(max_length=30,unique=True,null=True,blank=True)
    Vehicle_id = models.TextField(null=True,blank=True)
    fitness=models.TextField(null=True,blank=True)
    Vehicle_company = models.CharField(max_length=60,null=True,blank=True)
    Vehicle_colour = models.CharField(max_length=60,null=True,blank=True)
    Vehicle_model_year = models.CharField(max_length=60,null=True,blank=True)
    Vehicle_type = models.CharField(max_length=20,null=True,blank=True)
    Vehicle_capacity = models.IntegerField(null=True,blank=True)
    Vehicle_milage = models.CharField(max_length=10,null=True,blank=True)
    Vehicle_speed = models.CharField(max_length=20,null=True,blank=True)
    Vehicle_tonage = models.CharField(max_length=20,null=True,blank=True)
    Vehicle_total_axis = models.CharField(max_length=20,null=True,blank=True)
    Vehicle_uploaded_by = models.CharField(max_length=100,null=True,blank=True)
    # Vehicle_image1 = models.ImageField(upload_to='img/Vehicle_images/',null=True,blank=True)
    # Vehicle_image2 = models.ImageField(upload_to='img/Vehicle_images/')
    # Vehicle_image3 = models.ImageField(upload_to='img/Vehicle_images/')
    isGeared = models.TextField(null=True,blank=True)
    Vehicle_description = models.CharField(max_length=1500,null=True,blank=True)
    Vehicle_price = models.IntegerField(null=True,blank=True)
    is_anonymous=models.BooleanField(default=False,null=True,blank=True)
    is_authenticated=models.BooleanField(default=True,null=True,blank=True)
    USERNAME_FIELD = 'Vehicle_license_plate'
    REQUIRED_FIELDS = ['Vehicle_id', 
    'fitness', 'Vehicle_company','Vehicle_colour','Vehicle_model_year', 'Vehicle_type','Vehicle_capacity', 'Vehicle_milage',
     'Vehicle_speed','Vehicle_speed','Vehicle_tonage','Vehicle_total_axis','Vehicle_uploaded_by','Vehicle_image1','isGeared',
     'Vehicle_description','Vehicle_price'
    ]

    def __str__(self):
        return f"{self.Vehicle_license_plate} : {self.Vehicle_id}"
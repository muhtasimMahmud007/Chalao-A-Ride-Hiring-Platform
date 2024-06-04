from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyUserManagerCustomer(BaseUserManager):
    def create_user(self, uname,uid, nid,email,phone,bank,address,password=None):#uname,uid, nid,email,phone,bank,address,pass1//////self, email, password=None, **extra_fields
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(customer_name=uname,user_id=uid,NID=nid,email=email,phone=phone,bank_details=bank,address=address)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, uname,uid, nid,email,phone,bank,address,password=None):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(uname,uid, nid,email,phone,bank,address,password=password)

class MyUserCustomer(AbstractBaseUser):
    customer_name = models.CharField(max_length=255)
    user_id = models.CharField(unique=True, max_length=255)
    NID = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    bank_details = models.TextField()
    address = models.TextField()
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManagerCustomer()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['customer_name', 'user_id', 'NID', 'phone', 'bank_details', 'address']

    def __str__(self):
        return self.email

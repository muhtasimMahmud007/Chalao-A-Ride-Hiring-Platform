from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, uname,uid, nid,email,phone1,phone2,phone3,designation,share,address,password=None):#uname,uid, nid,email,phone,bank,address,pass1//////self, email, password=None, **extra_fields
         if not email:
             raise ValueError('The Email field must be set')
         email = self.normalize_email(email)
         user = self.model(owner_name=uname,user_id=uid,NID=nid,email=email,phone1=phone1,phone2=phone2,phone3=phone3,designation=designation,share=share,address=address)
         user.set_password(password)
         user.save(using=self._db)
         return user
    # def create_superuser(self, uname, uid, nid, email, phone1, phone2, phone3, designation, share, address, password):
    #      if not email:
    #          raise ValueError('The Email field must be set')
    #      email = self.normalize_email(email)
    #      user = self.model(uname,uid,nid,email,phone1,phone2,phone3,designation,share,address)
    #      user.set_password(password)
    #      user.save(using=self._db)
    #      return user
    def create_superuser(self, owner_name, user_id, NID, email, phone1, phone2, phone3, designation, share, address, password=None):
        if not email:
          raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(owner_name=owner_name, user_id=user_id, NID=NID, email=email, phone1=phone1, phone2=phone2, phone3=phone3, designation=designation, share=share, address=address, is_admin=True, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser):
    owner_name = models.CharField(max_length=255)
    user_id = models.CharField(unique=True, max_length=255)
    NID = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone1 = models.CharField(max_length=255)
    phone2 = models.CharField(max_length=255,null=True,blank=True)
    phone3 = models.CharField(max_length=255,null=True,blank=True)
    designation = models.TextField()
    share = models.IntegerField()
    address=models.TextField()
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'owner_name','user_id', 'NID', 'phone1','phone2','phone3', 'designation','share', 'address']


    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
         return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

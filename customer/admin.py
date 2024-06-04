from django.contrib import admin as c_admin
from .models import MyUserCustomer

# Register your models here.
c_admin.site.register(MyUserCustomer)

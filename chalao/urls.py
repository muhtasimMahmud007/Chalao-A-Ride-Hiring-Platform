# from registration import views as r_views
from django.urls import path, include
from django.contrib import admin as real_admin
# from customer import views as c_views
# from employee import views as e_views

urlpatterns = [
    path('20101524admin/', real_admin.site.urls),
    path('20301481admin/', real_admin.site.urls),
    path('20101122admin/', real_admin.site.urls),
    path('22241185admin/', real_admin.site.urls),

    path('',include("registration.urls"), name='choice'),
    path('customer/',include('customer.urls')),
    path('employee/',include('employee.urls')),
    path('book/',include('book.urls')),



    path('20101524/owner/', include('owner.urls')),
    path('20301481/owner/', include('owner.urls')),
    path('22241185/owner/', include('owner.urls')),
    path('20101122/owner/', include('owner.urls')),
    
    path('20101524/vehicles/', include('vehicles.urls')),
    path('20301481/vehicles/', include('vehicles.urls')),
    path('20101122/vehicles/', include('vehicles.urls')),
    path('22241185/vehicles/', include('vehicles.urls')),
]
# path('customer/', include('customer.urls')),
#     path('employee/', include('employee.urls')),
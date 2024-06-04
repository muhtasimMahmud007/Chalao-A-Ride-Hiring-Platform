from django.urls import path,include
from customer import views as c_views
from employee import views as e_views
from registration import views as re_views


urlpatterns = [
    path('', re_views.Choicepage, name='choice'),
    path('customer/', c_views.SignupPageCustomer, name='customer'),
    path('employee/', e_views.SignupPageEmployee, name='employee'),
    ]
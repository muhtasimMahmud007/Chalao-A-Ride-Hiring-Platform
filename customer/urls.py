from django.urls import path
from customer import views as cus_views
from book import views as book_views



urlpatterns = [
    path('',cus_views.SignupPageCustomer,name='c_signup'),
    path('c_profile/',cus_views.ProfilePageCustomer,name='c_profile'),
    path('c_login/',cus_views.LoginPageCustomer,name="c_login"),
    path('c_home/',cus_views.HomePageCustomer,name='c_home'),
    path('c_logout/',cus_views.LogoutPageCustomer,name='c_logout'),
    path('book/',book_views.book_ride,name='book'),
    path('cus_delete/',cus_views.DeleteCustomer,name='cus_delete'),

]
from django.urls import path
from employee import views as em_views



urlpatterns = [
    path('',em_views.SignupPageEmployee,name='e_signup'),
    path('e_profile/',em_views.ProfilePageEmployee,name='e_profile'),
    path('e_login/',em_views.LoginPageEmployee,name="e_login"),
    path('e_home/',em_views.HomePageEmployee,name='e_home'),
    path('e_logout/',em_views.LogoutPageEmployee,name='e_logout'),

]
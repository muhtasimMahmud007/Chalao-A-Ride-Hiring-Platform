from django.urls import path
from owner import views as o_views



urlpatterns = [
    path('',o_views.SignupPage,name='signup'),
    path('profile/',o_views.ProfilePage,name='profile'),
    path('login/',o_views.LoginPage,name="login"),
    path('home/',o_views.HomePage,name='home'),
    path('logout/',o_views.LogoutPage,name='logout'),

]
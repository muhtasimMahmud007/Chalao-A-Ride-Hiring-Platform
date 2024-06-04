from django.urls import path
from vehicles import views as v_views



urlpatterns = [
    path('',v_views.upload_vehicle,name='upload'),
    path('v_profile/',v_views.Profile_Page,name='v_profile'),

]
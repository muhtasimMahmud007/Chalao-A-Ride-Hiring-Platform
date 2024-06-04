from django.urls import path
from book import views as book_views



urlpatterns = [
    path('book/',book_views.book_ride,name='book'),
    path('booking_success/',book_views.booking_success,name='booking_success'),
    path('payment/',book_views.payment,name='payment'),

]
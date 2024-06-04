# from django.shortcuts import render, redirect
# from .models import Booking
# from .forms import BookingForm

# def book_ride(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('booking_success')
#     else:
#         form = BookingForm()
#     context = {'form': form}
#     return render(request, 'book.html', context)

# def booking_success(request):
#     return render(request, 'booking_success.html')

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.shortcuts import get_object_or_404

# Create your views here.
def book_ride(request):

    customer_email = request.POST.get('email')
    pickup_location = request.POST.get('pick')
    destination = request.POST.get('des')
    distance = request.POST.get('dis')
    pickup_date = request.POST.get('pd')
    pickup_time = request.POST.get('pt')
    num_passengers = request.POST.get('num')
    vehicle_type = request.POST.get('vt')
    if vehicle_type=="bus":
            User.total_amount = (int(distance)*5)*(int(num_passengers))
    if vehicle_type=="bike":
            User.total_amount = int(distance)*50
    if vehicle_type=="truck":
            User.total_amount = int(distance)*40
    if vehicle_type=="micro bus":
            User.total_amount = int(distance)*30
    if vehicle_type=="private car":
            User.total_amount = int(distance)*40

    result_book = Booking.objects.filter(customer_email=customer_email)
    book=Booking(customer_email=customer_email,pickup_location=pickup_location,destination=destination,distance=distance,
                pickup_date=pickup_date,pickup_time=pickup_time,num_passengers=num_passengers,vehicle_type=vehicle_type)


    book.save()
    return render(request, 'book.html')

# def booking_success(request):
#     context={'a':User.pick,'b':User.destination,'c':User.distance,'d':User.pickup_date,'e':User.pickup_time,
#     'f':User.num_passengers,'g':User.vehicle_type,'h':User.customer_email,'i':User.total_amount}
#     return render(request, 'booking_success.html',context)
def booking_success(request):
    context={'a':User.total_amount}
    return render(request, 'booking_success.html',context)

def payment(request):
    return render(request, 'payment.html')
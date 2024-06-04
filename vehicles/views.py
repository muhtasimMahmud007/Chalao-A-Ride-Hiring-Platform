from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from django.shortcuts import get_object_or_404

# Create your views here.
def upload_vehicle(request):
    Vehicle_license_plate = request.POST.get('license')
    Vehicle_id = request.POST.get('vid')
    fitness=request.POST.get('fit')
    Vehicle_company = request.POST.get('comp')
    Vehicle_colour = request.POST.get('color')
    Vehicle_model_year = request.POST.get('year')
    Vehicle_type = request.POST.get('type')
    Vehicle_capacity = request.POST.get('cap')
    Vehicle_milage = request.POST.get('mile')
    Vehicle_speed = request.POST.get('speed')
    Vehicle_tonage = request.POST.get('ton')
    Vehicle_total_axis = request.POST.get('axis')
    Vehicle_uploaded_by= request.POST.get('owner')
    Vehicle_image1 = request.POST.get('image')
    # Vehicle_image2 = models.ImageField(upload_to='img/Vehicle_images/')
    # Vehicle_image3 = models.ImageField(upload_to='img/Vehicle_images/')
    isGeared = request.POST.get('gear')
    Vehicle_description = request.POST.get('desc')
    Vehicle_price = request.POST.get('price')
    result_vehicle = Vehicle.objects.filter(Vehicle_license_plate=Vehicle_license_plate)

    vehicle=Vehicle(Vehicle_license_plate=Vehicle_license_plate,Vehicle_id=Vehicle_id,fitness=fitness,
        	Vehicle_company=Vehicle_company,Vehicle_colour=Vehicle_colour,
        	Vehicle_model_year=Vehicle_model_year,Vehicle_type=Vehicle_type,Vehicle_capacity=Vehicle_capacity,
        	Vehicle_milage=Vehicle_milage,Vehicle_speed=Vehicle_speed,Vehicle_tonage=Vehicle_tonage,Vehicle_total_axis=Vehicle_total_axis,
        	Vehicle_uploaded_by=Vehicle_uploaded_by,isGeared=isGeared,Vehicle_description=Vehicle_description,Vehicle_price=Vehicle_price)#here image before price
    vehicle.save()
    return render(request,'owner_upload_vehicle.html')

    # return render (request,'vehicle_profile.html')
    # if result_vehicle:
    #     if Vehicle_uploaded_by.exists():
    #         Message = "This Vehicle already exist!!"
    #         return render(request,'vehicle_profile.html')
    # else:
def Profile_Page(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles}
    return render(request, 'vehicle_profile.html', context)
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import MyUser
# Create your views here.
@login_required(login_url='owner_login')
def HomePage(request):
    return render (request,'owner_home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        uid=request.POST.get('userid')
        nid=request.POST.get('usernid')
        email=request.POST.get('email')
        phone1=request.POST.get('phone1')
        phone2=request.POST.get('phone2')
        phone3=request.POST.get('phone3')
        designation=request.POST.get('designation')
        share=request.POST.get('share')
        address=request.POST.get('useraddress')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=MyUser.objects.create_user(uname,uid, nid,email,phone1,phone2,phone3,designation,share,address,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'owner_signup.html')

def LoginPage(request):
    if request.method=='POST':
        user=request.POST.get('email')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=user,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
             # print("Username or Password is incorrect!!!")
             return redirect('login')

    return render (request,'owner_login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
def ProfilePage(request):
    return render (request,'owner_profile.html')
from django.shortcuts import render,HttpResponse,redirect


def Choicepage(request):
    return render(request,"choice.html")

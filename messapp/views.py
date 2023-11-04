from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    return render(request,"index.html")

def user_register(request):
    if request.method=="POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")

        user=User.objects.create_user(
            username=uname,
            password=passw,
            is_customer=True, 

        )
        return redirect('index')
    
    else:

        return render(request, "user_register.html")

def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        passw=request.POST.get('password')

        user=User.objects.filter(username=uname).first()
        if user is not None and user.check_password(passw) and user.is_customer:
            login(request,user)
            return redirect('user_home')
        else:
            messages.error(request, 'Invalid')

    return render(request,"user_login.html")

def user_home(request):
    return render(request,"user_home.html")


def signout(request):
    logout(request)
    return redirect('index')   


def mess_register(request):
    if request.method=="POST":
        uname = request.POST.get("username")
        passw = request.POST.get("password")

        user=User.objects.create_user(
            username=uname,
            password=passw,
            is_mess=True, 

        )
        return redirect('index')
    
    else:

        return render(request, "mess_register.html")
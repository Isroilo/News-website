from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from dashboard.models import *

def signin_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        print(usr, username, password)
        if usr is not None:
            login(request,usr)
            return redirect('index_url')
    return render(request, 'account/log-in.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username,password=password)
        return redirect('index_url')
    return render(request,'account/register.html')


def logout_view(request):
    logout(request)
    return redirect('index_url')
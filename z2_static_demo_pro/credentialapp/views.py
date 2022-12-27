from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email id exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=f_name,
                                                last_name=l_name, email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password mismatching')
            return redirect('register')


    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

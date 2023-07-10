from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import UserForm
from .models import user_details
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def restaurant(request):
    return render(request, 'restaurant.html')

def booking(request):
    return render(request, 'booking.html')

def pricing(request):
    return render(request, 'pricing.html')

def cars(request):
    return render(request, 'cars.html')

def profile(request, driver):
    drivers = {
        'sudhin': {
            'name': 'Sudhin S',
            'image': 'sudhin.jpg',
            'mobile': '00000',
            'address': 'Amrita',
            'email': 'sudi@gmail.com',
            'health': 'good',
            'country': 'India',
            'state': 'Kerala'
        },
        'dhanush': {
            'name': 'Dhanush Krishna R',
            'image': 'dhanush.png',
            'mobile': '111111',
            'address': 'Amrita',
            'email': 'dhanush@gmail.com',
            'health': 'good',
            'country': 'India',
            'state': 'Kerala'
        },
        'athul': {
            'name': 'Athul Gireesh',
            'image': 'athul.jpeg',
            'mobile': '22222222',
            'address': 'Amrita',
            'email': 'athul@gmail.com',
            'health': 'good',
            'country': 'India',
            'state': 'Kerala'
        },
        'nanditha': {
            'name': 'Nanditha',
            'image': 'nanditha.jpg',
            'mobile': '33333333',
            'address': 'Amrita',
            'email': 'nanditha@gmail.com',
            'health': 'good',
            'country': 'India',
            'state': 'Kerala'
        },
        'gps': {
            'name': 'GPS',
            'image': 'gps.jpeg',
            'mobile': '444444',
            'address': 'Amrita',
            'email': 'gps@gmail.com',
            'health': 'good',
            'country': 'India',
            'state': 'Kerala'
        },
        'dhruv': {
            'name': 'Dhruv RK',
            'image': 'dhruv.jpeg',
            'mobile': '55555',
            'address': 'Amrita',
            'email': 'drk@gmail.com',
            'health': 'good',
            'country': 'India',
            'state': 'Kerala'
        },
        'adithya': {
            'name': 'Adithya S Nair',
            'image': 'adithya.jpg',
            'mobile': '66666',
            'address': 'Amrita',
            'email': 'adi@gmail.com',
            'health': 'good',
            'country': 'India',
            'state': 'Kerala'
        },
    }
    driver_data = drivers.get(driver.lower())
    return render(request, 'profile.html', context=driver_data)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            username = User.objects.get(email=email).username
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Invalid username or password')
                return redirect('login')
        except User.DoesNotExist:
            messages.info(request, 'You are not registered on this website')
            return redirect('signup')
    else:  
        return render(request, 'login.html')
    
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        conf_password=request.POST['conf_password']
        username= firstname +" "+lastname
    
        if password == conf_password:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Mail ID already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, first_name = firstname, last_name=lastname, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('signup.html')
    else:
        return render(request,'signup.html')


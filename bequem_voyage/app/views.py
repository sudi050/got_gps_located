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
                messages.info(request,'College ID already exists')
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


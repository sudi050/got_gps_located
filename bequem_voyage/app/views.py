from django.shortcuts import render
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
        college_mail = request.POST['college_mail']
        password = request.POST['password']
        
        try:
            username = User.objects.get(email=college_mail).username
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                
                if user_details.objects.filter(college_mail=college_mail).exists():
                    return redirect('index')
                else:
                    return redirect('add_user')
            
            else:
                messages.info(request, 'Invalid username or password')
                return redirect('login')
        
        except User.DoesNotExist:
            messages.info(request, 'You are not registered on this website')
            return redirect('signup')

    return render(request, 'login.html')

  

def signup(request):
    if request.method == 'POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        college_mail=request.POST['college_mail']
        password=request.POST['password']
        conf_password=request.POST['conf_password']
        username= firstname +" "+lastname
        
        if password_check(password):
            if password == conf_password:
                if User.objects.filter(email=college_mail).exists():
                    messages.info(request,'College ID already exists')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, first_name = firstname, last_name=lastname, email=college_mail, password=password)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request,'Password not matching')
                return redirect('signup')
        else:
            messages.info(request,'''Please enter a password that is at least 6 characters long, 
                          contains at least one uppercase letter and one alphanumeric character.''')
            return redirect('signup')
    else:
        return render(request,'signup.html')

def password_check(passwd):
    SpecialSym =['!', '@', '#', '$', '%', '~','&']
    val = True
    if len(passwd) < 6:
        val = False  
    if len(passwd) > 20:
        val = False  
    if not any(char.isdigit() for char in passwd):
        val = False 
    if not any(char.isupper() for char in passwd):
        val = False  
    if not any(char.islower() for char in passwd):
        val = False   
    if not any(char in SpecialSym for char in passwd):
        val = False
    if val:
        return val

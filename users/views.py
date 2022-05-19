from atexit import register
from multiprocessing import context
from django.shortcuts import render , redirect
from . models import Profile, Skill
from projects.models import Project
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from . forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def profiles(request):
    profiles  = Profile.objects.all()
    context={
        'profiles' : profiles,
    }
    return render(request, 'users/profiles.html',context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {
        'profile':profile,
    }
    return render(request,'users/user_profile.html',context)

def userlogin(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Welcome home!')
            return redirect('profiles')
        else:
            messages.error(request,'Username or Password is incorrect.')    

    else:
        return render(request,'users/login_register.html')    

def userlogout(request):
    logout(request)
    messages.success(request,'User logged out.')   
    return redirect('profiles')    


def userregister(request):
    form = CustomUserCreationForm()
    page = 'register'

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request,"User account created!")
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error while registration.')

           
    context  = {
            'form':form,
            'page':page,
        }
    return render(request,'users/login_register.html' ,context) 
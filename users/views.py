from multiprocessing import context
from django.shortcuts import render
from . models import Profile, Skill
from projects.models import Project

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
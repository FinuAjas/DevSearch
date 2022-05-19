from cProfile import label
from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ['fisrt_name','email','username','password1','password2']
        fields = ['email','username','password1','password2']
        labels = {
            'first_name':'First Name',
            'email': 'Email',
        }

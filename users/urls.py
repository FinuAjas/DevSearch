from django.urls import path
from . import views

urlpatterns = [
    path('',views.profiles,name='profiles'),
    path('user_profile/<str:pk>/',views.user_profile,name='user_profile'),
    path('login/',views.userlogin,name='userlogin'),
    path('register/',views.userregister,name='userregister'),
    path('logout/',views.userlogout,name='userlogout'),
]
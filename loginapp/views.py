from django.shortcuts import render
from .forms import ProfileInfoForm
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def register(request):
    registered = False
    if request.method == "POST":
        registered =True
        profile_form = ProfileInfoForm(request.POST)
        if profile_form.is_valid():
            username = profile_form.cleaned_data['username']
            password = profile_form.cleaned_data['password']
            print(username)
            print(password)
            # print(password)
            user = User()
            user.username = username
            print(user.username)
            user.set_password(password)
            user.save()
            portfolio_url = profile_form.cleaned_data['portfolio_url']
            profile = Profile()
            profile.portfolio_url = portfolio_url
            profile.user = user
           
            profile.save()
          
            
        else:
            print(profile_form.errors)
    else:
        profile_form = ProfileInfoForm()
    print(registered)
    return render(request,"loginapp/register.html",{'profile_form':profile_form,'registered':registered})

def index(request):
    return render(request,"loginapp/index.html")

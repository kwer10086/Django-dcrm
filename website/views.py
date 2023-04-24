from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.


def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request,'You Have Been Logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Username or Password error...')
            return redirect('home')
    else:
        return render(request,'home.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,'you have been logged out...')
    return redirect('home')


def register(request):



    return render(request, 'register.html', {})

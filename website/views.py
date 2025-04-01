from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupUserForm

def getting_started(request):
    return render(request, 'getting_started.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('item:home')
        else:
            return redirect('website:user_login')
        
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('website:user_login')

def user_signup(request):
    if request.method == "POST":
        form = SignupUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('website:user_login') 
        
    else:
        form = SignupUserForm()
    
    return render(request, 'signup.html', {
        'form': form
    })
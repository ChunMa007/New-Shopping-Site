from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import SignupUserForm, UserProfileForm, EditUserForm
from django.contrib.auth.models import User
from .models import Profile

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
        
    return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return redirect('website:user_login')

def user_signup(request):
    if request.method == "POST":
        user_form = SignupUserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('website:user_login') 
        
    else:
        user_form = SignupUserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
      
    return render(request, 'profile.html', {
        'user': user
    })
    
def edit_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)
    
    if request.method == "POST":
        user_form = EditUserForm(request.POST or None, instance=user)
        profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            return redirect('website:profile', pk=pk)
    else:
        user_form = EditUserForm(instance=user)
        profile_form = UserProfileForm(instance=profile)
    
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
            
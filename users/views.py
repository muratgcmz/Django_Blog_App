from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from .forms import UserForm, UserProfileForm, UpdateProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return render(request, 'user/logout.html')
    
def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    
    if form.is_valid():
        user = form.get_user()

        if user :
            messages.success(request, 'login successfull')
            login(request, user)
        return redirect('home')

    return render(request, 'user/user_login.html',{"form": form})

def register(request):
    form_user = UserForm()
    

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        

        if form_user.is_valid():
            user = form_user.save()
            
            login(request, user)
            messages.success(request, 'Register Successfull')
            return redirect('home')
    context={
        'form_user': form_user,
        
    }

    return render(request, 'user/register.html', context)

@login_required(login_url="/user/login/")
def profile(request):
    if request.method == 'POST':
        user_form = UserProfile(request.POST, instance=request.user)
        update_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
    
        if user_form.is_valid() and update_form.is_valid():
            user_form.save()
            update_form.save()
            messages.success(request, 'Your profile updated successfully.')
            return redirect('home')
    else:
        user_form = UserProfile(instance=request.user)
        update_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'user/profile.html', {'user_form': user_form, 'update_form': update_form})
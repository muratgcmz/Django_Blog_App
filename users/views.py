from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from .forms import UserForm, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
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


def profile(request, id):
    try:
        userprofile = UserProfile.objects.get(id=id)
    except:
        userprofile = None
    form_profile = UserProfileForm(request.POST or None, request.FILES or None, instance=userprofile)
    if form_profile.is_valid():
        profileTemp = form_profile.save()
        if 'image' in request.FILES:
            profileTemp.image = request.FILES.get('image')
            profileTemp.save()
        return redirect('home')
    context = {
        'form_profile': form_profile,
        'user': userprofile 
        }
    return render(request, 'user/profile.html', context)

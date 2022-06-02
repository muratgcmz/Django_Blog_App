from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return render(request, 'user/logout.html')
    
def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    
    if form.is_valid():
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password')
        # user = authenticate(username=username, password=password)

        user = form.get_user()

        if user :
            messages.success(request, 'login successfull')
            login(request, user)
        return redirect('home')

    return render(request, 'user/user_login.html',{"form": form})
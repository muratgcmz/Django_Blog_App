from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.


def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return redirect('home')
    
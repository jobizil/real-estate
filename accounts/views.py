from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        messages.error(request, 'This is a test message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

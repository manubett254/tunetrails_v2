# dashboard/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, 'dashboard/home.html')

def courses(request):
    return render(request, 'dashboard/courses.html')

def lessons(request):
    return render(request, 'dashboard/lessons.html')

def practice(request):
    return render(request, 'dashboard/practice.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

@login_required
def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard:home')
        else:
            return render(request, 'dashboard/login.html', {'error': 'Invalid credentials'})
    # GET request renders login page
    return render(request, 'dashboard/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('dashboard:login')



def welcome(request):
    # Page users land on after successful login
    return render(request, 'dashboard/welcome.html')

# dashboard/views.py
from django.shortcuts import render

def signup_view(request):
    return render(request, 'dashboard/signup.html')

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
    # Firebase config context
    context = {
        'FIREBASE_API_KEY': settings.FIREBASE_API_KEY,
        'FIREBASE_AUTH_DOMAIN': settings.FIREBASE_AUTH_DOMAIN,
        'FIREBASE_PROJECT_ID': settings.FIREBASE_PROJECT_ID,
        'FIREBASE_STORAGE_BUCKET': settings.FIREBASE_STORAGE_BUCKET,
        'FIREBASE_MESSAGING_SENDER_ID': settings.FIREBASE_MESSAGING_SENDER_ID,
        'FIREBASE_APP_ID': settings.FIREBASE_APP_ID,
        'FIREBASE_MEASUREMENT_ID': settings.FIREBASE_MEASUREMENT_ID,
    }

    if request.method == 'POST':
        username = request.POST.get('username') or request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard:home')
        else:
            context['error'] = 'Invalid credentials'

    return render(request, 'dashboard/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('dashboard:login')



def welcome(request):
    # Page users land on after successful login
    return render(request, 'dashboard/welcome.html')

# dashboard/views.py
from django.shortcuts import render
from django.conf import settings
def signup_view(request):
    return render(request, 'dashboard/signup.html')


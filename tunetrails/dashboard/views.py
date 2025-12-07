from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'dashboard/login.html')

def welcome_view(request):
    return render(request, 'dashboard/welcome.html')

def home_view(request):
    return render(request, 'dashboard/home.html') 

def courses_view(request):
    return render(request, 'dashboard/courses.html')

def lessons_view(request):
    return render(request, 'dashboard/lessons.html')

def practice_view(request):
    return render(request, 'dashboard/practice.html')

def signup_view(request):
    return render(request, 'dashboard/signup.html')
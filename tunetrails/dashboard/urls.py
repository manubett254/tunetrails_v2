from django.urls import path
from dashboard import views

app_name = 'dashboard'  # important for namespacing

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('lessons/', views.lessons, name='lessons'),
    path('practice/', views.practice, name='practice'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('signup/', views.signup_view, name='signup'),
]

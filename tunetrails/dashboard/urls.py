from django.urls import path
from dashboard import views

app_name = 'dashboard'  # THIS IS IMPORTANT

urlpatterns = [
    path('', views.welcome_view, name='welcome'), 
    path('login/', views.login_view, name='login'),  # root page shows login
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
    path('courses/', views.courses_view, name='courses'),
    path('lessons/', views.lessons_view, name='lessons'),
    path('practice/', views.practice_view, name='practice'),

]


# dashboard/context_processors.py
from django.templatetags.static import static
from django.urls import reverse

def core_urls(request):
    return {
        'login_url': reverse('dashboard:login'),
        'welcome_url': reverse('dashboard:welcome'),
        'home_url': reverse('dashboard:home'),
        'profile_url': reverse('dashboard:profile'),
        'default_avatar': static('dashboard/images/default_user.png'),
    }
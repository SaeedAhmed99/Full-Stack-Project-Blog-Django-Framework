from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, register_back, log_in, log_out, profile, profile_update
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('register/', register, name='register' ),
    path('register_back/', register_back, name='register_back'),
    #path('login/', LoginView.as_view(template_name = 'user/log_in.html'), name='login'),
    #path('logout/', LogoutView.as_view(template_name = 'user/log_out.html'), name='logout'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    #path('log_in_backend/', log_in_backend, name='login_backend'),
    path('profile/', profile, name='profile'),
    path('profile_update/', profile_update, name='profile_update'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

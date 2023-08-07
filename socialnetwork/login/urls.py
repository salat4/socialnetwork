from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views

app_name = 'login'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),  # Додайте маршрут для реєстрації
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Сторінка "home" в кореневому URL-і
]
"""Define URL schemes for users"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from . import views

app_name = "users"

urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    # Logout page
    path('logout/', views.logout_view, name="logout"),
    # Register page
    path('register/', TemplateView.as_view(template_name='users/register.html'), name="register"),
]

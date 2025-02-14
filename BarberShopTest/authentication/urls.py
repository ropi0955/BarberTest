from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile, home

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="authentication/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("profile/", profile, name="profile")
]

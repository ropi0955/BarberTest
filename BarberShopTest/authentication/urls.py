# from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
# from .views import register, profile, home

# urlpatterns = [
#     path("register/", register, name="register"),
#     path("login/", LoginView.as_view(template_name="authentication/login.html"), name="login"),
#     path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
#     path("profile/", profile, name="profile")
# ]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile, home

urlpatterns = [
    # path("login/", views.user_login, name="login"),  # Bejelentkezés
    path("login/", LoginView.as_view(template_name="authentication/login.html"), name="login"),
    # path("register/", views.user_register, name="register"),  # Regisztráció
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),  # Kijelentkezés után főoldalra irányítás
    path("profile/", profile, name="profile"),  # Profil oldal
]


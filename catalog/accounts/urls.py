from django.urls import path, include

from .views import register, login_view, logout_view, profile

app_name = "accounts"


urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name = "login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile, name="profile")
]
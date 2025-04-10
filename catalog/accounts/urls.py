<<<<<<< HEAD
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

from .views import (
    register,
    login_view,
    logout_view,
    profile,
    edit_profile_view,
    confirm_email,
)

app_name = "accounts"


=======
from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from .views import register, login_view, logout_view, profile

app_name = "accounts"

>>>>>>> 4b18188892c36b6b01568f971ad0f2cd895fdbbf
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
<<<<<<< HEAD
    path("edit_profile/", edit_profile_view, name="edit_profile"),
    path("profile/", profile, name="profile"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
=======
    path("profile/", profile, name="profile"),
    path("password_change/",
        PasswordChangeView.as_view(
>>>>>>> 4b18188892c36b6b01568f971ad0f2cd895fdbbf
            success_url=reverse_lazy("accounts:password_change_done"),
            template_name="password_change.html",
        ),
        name="password_change",
    ),
<<<<<<< HEAD
    path(
        "password_change_done",
        auth_views.PasswordChangeDoneView.as_view(
=======
    path("password_change_done",
        PasswordChangeDoneView.as_view(
>>>>>>> 4b18188892c36b6b01568f971ad0f2cd895fdbbf
            template_name="password_change_done.html"
        ),
        name="password_change_done",
    ),
<<<<<<< HEAD
    path("confirm_email", confirm_email, name="confirm_email"),
]
=======
]
>>>>>>> 4b18188892c36b6b01568f971ad0f2cd895fdbbf

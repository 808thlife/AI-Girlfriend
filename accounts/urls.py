from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/submit", views.login_view, name = "login_view"),
    path("signup/", views.signup_view, name = "signup_view"),
    path("logout/", views.logout_view, name = "logout_view")
]

from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name = "index"),
    path("chat/<str:hash>", views.chat_view, name = "chat"),
    path("create/", views.delete_chat, name = "delete_chat"),
    path("login/", views.login_view, name = "login_view"),
    path("signup/", views.signup_view, name = "signup_view")
]

from django.urls import path
from . import views


urlpatterns = [
    path("main/", views.main_view, name="main"),
    path("auth/register/", views.register_view, name="register"),
    path("auth/confirmEmail/", views.confirm_email_view, name="confirmEmail"),
    path("auth/login/", views.login_view, name="login"),
]

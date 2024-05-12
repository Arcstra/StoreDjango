from django.urls import path
from . import views


urlpatterns = [
    path("auth/register/", views.create_user_view, name="createUser"),
    path("auth/confirmEmail/", views.ConfirmEmailView.as_view(), name="confirmEmail"),
    path("auth/login/", views.login_view, name="login"),
    path("auth/logout/", views.logout_view, name="logout"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("auth/register/", views.create_user_view, name="createUser"),
    path("auth/confirmEmail/", views.ConfirmEmailView.as_view(), name="confirmEmail"),
]
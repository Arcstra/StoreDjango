from django.http import HttpRequest, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.core.cache import cache
from django.views import View
from .forms import RegisterForm, CodeFromEmailForm, LoginForm
from .models import User
from .tasks import sendCodeToEmail
import json


def create_user_view(request : HttpRequest):
    form = RegisterForm(request.POST)

    if not form.is_valid():
        print(form.errors)
        return JsonResponse({}, status=400)
    
    try:
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
    except Exception as e:
        print(e)
        return JsonResponse({}, status=400)
    
    login(request, user)
    
    return JsonResponse({"id": user.id}, status=201)


class ConfirmEmailView(View):
    @staticmethod
    def get(request : HttpRequest):
        import random
        code = str(random.randint(100000, 999999))
        cache.delete(request.user.email, 0)
        cache.set(request.user.email, code, 60*2, 0)

        sendCodeToEmail.delay(request.user.email, code)
        return JsonResponse({}, status=200)

    @staticmethod
    def post(request : HttpRequest):
        form = CodeFromEmailForm(request.POST)

        if not form.is_valid():
            return JsonResponse({}, status=400)

        try:
            user = User.objects.get(id=request.user.id)
        except:
            return JsonResponse({}, status=404)
        
        code = cache.get(user.email)

        if not code == form.cleaned_data["code"]:
            return JsonResponse({}, status=400)
        
        user.confirmed_email = True
        user.save()

        return JsonResponse({}, status=200)
    

def login_view(request : HttpRequest):
    form = LoginForm(request.POST)

    if not form.is_valid():
        return JsonResponse({}, status=400)
    
    username = form.cleaned_data["username"]
    password = form.cleaned_data["password"]

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({}, status=404)
    
    login(request, user)

    return JsonResponse({}, status=200)


def logout_view(request : HttpRequest):
    logout(request)
    return JsonResponse({}, status=200)

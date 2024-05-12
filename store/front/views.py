from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from .forms import RegisterForm, CodeFromEmailForm


def main_view(request):
    template = loader.get_template("main.html")
    context = {

    }
    return HttpResponse(template.render(context, request))


def register_view(request):
    template = loader.get_template("register.html")
    context = {
        "form": RegisterForm(),
    }
    return HttpResponse(template.render(context, request))


def confirm_email_view(request):
    template = loader.get_template("confirmEmail.html")
    context = {
        "form": CodeFromEmailForm(),
    }
    return HttpResponse(template.render(context, request))

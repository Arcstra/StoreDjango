from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "username_display", "email", "password", )

    username = forms.CharField(max_length=255)
    username_display = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=forms.widgets.PasswordInput())
    password_again = forms.CharField(widget=forms.widgets.PasswordInput())

    def is_valid(self) -> bool:
        return super().is_valid() \
            and self.cleaned_data["password"] == self.cleaned_data["password_again"]

class CodeFromEmailForm(forms.Form):
    code = forms.CharField(max_length=6)
    
from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255)
    username_display = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=forms.widgets.PasswordInput())
    password_again = forms.CharField(widget=forms.widgets.PasswordInput())


class CodeFromEmailForm(forms.Form):
    code = forms.CharField(max_length=6)

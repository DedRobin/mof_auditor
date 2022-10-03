from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='Username')
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())

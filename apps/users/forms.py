from django import forms

from apps.profiles.models import GENDER_CHOICE


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    gender = forms.ChoiceField(choices=GENDER_CHOICE, required=False)
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label="Username")
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())

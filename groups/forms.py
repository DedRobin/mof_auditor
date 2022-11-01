from django import forms

from profiles.models import GENDER_CHOICE


class CreateGroupForm(forms.Form):
    # GroupInformation
    name = forms.CharField(max_length=150)
    description = forms.CharField(max_length=255)

    # Group

    username = forms.CharField(max_length=150)
    gender = forms.ChoiceField(choices=GENDER_CHOICE, required=False)
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='Username')
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())

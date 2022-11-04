from django import forms

from apps.profiles.models import GENDER_CHOICE


class ProfileForm(forms.Form):
    username = forms.CharField(max_length=150, required=False)
    # password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICE, required=False)

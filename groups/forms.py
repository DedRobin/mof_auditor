from django import forms


class CreateGroupForm(forms.Form):
    name = forms.CharField(max_length=150)
    description = forms.CharField(max_length=255)

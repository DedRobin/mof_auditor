from django import forms
from django.db.models import QuerySet

from apps.groups.models import Group


class CreateGroupForm(forms.Form):
    name = forms.CharField(max_length=150)
    description = forms.CharField(max_length=255)


class EditGroupForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField()
    # invited_users = forms.ModelMultipleChoiceField(
    #         widget=forms.CheckboxSelectMultiple,
    #         queryset=None
    #     )

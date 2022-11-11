from django import forms

from apps.groups.models import Group, GroupInformation


class CreateGroupForm(forms.Form):
    name = forms.CharField(
        max_length=150,
    )
    description = forms.CharField(
        max_length=255,
    )


class EditGroupInformationForm(forms.Form):
    name = forms.CharField(
        max_length=150,
    )
    description = forms.CharField(
        max_length=255,
    )

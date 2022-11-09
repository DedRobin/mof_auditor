from django import forms

from apps.groups.models import Group, GroupInformation


class CreateGroupForm(forms.Form):
    name = forms.CharField(max_length=150)
    description = forms.CharField(max_length=255)


class EditGroupInformationForm(forms.ModelForm):
    class Meta:
        model = GroupInformation
        fields = (
            "name",
            "description",
        )


class EditGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        edit_only = True
        fields = (
            "invited_users",
            "permissions",
        )
        widgets = {
            "invited_users": forms.CheckboxSelectMultiple(),
            "permissions": forms.CheckboxSelectMultiple(),
        }

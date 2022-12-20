from django import forms

from apps.groups.models import GroupInformation


class CreateGroupInformationForm(forms.ModelForm):
    class Meta:
        model = GroupInformation
        fields = (
            "name",
            "description",
        )


class EditGroupInformationForm(forms.ModelForm):
    class Meta:
        model = GroupInformation
        fields = (
            "name",
            "description",
        )

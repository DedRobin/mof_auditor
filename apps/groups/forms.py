from django import forms

from apps.groups.models import GroupInformation

GROUP_TYPE = [
    ("mine", "Only mine"),
    ("not mine", "Excluding mine"),
]


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


class GroupFilterForm(forms.Form):
    by_name = forms.CharField(required=False, max_length=255)
    created_at_from = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
            },
            # format="%Y-%m-%d %H:%M",
        ),
    )
    created_at_to = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
            },
            # format="%Y-%m-%d %H:%M",
        ),
    )
    group_type = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=GROUP_TYPE, required=False
    )

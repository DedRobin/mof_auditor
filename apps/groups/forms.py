from django import forms

from apps.groups.models import Group, GroupInformation


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

# class EditGroupForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         qs = kwargs.pop('invited_users')
#         super(EditGroupForm, self).__init__(*args, **kwargs)
#         self.fields['invited_users'].queryset = qs
#
#     class Meta:
#         model = Group
#         invited_users = forms.ModelMultipleChoiceField(
#             queryset=None,
#         )
#         fields = (
#             "invited_users",
#         )

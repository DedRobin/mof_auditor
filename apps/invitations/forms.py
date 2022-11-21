from django import forms


class SendInvitationForm(forms.Form):
    to_who = forms.CharField(max_length=255)

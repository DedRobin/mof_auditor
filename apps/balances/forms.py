from django import forms
from django.conf import settings

from apps.balances.models import Currency, Balance


class CurrencyConvertForm(forms.Form):
    from_amount = forms.DecimalField(
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
    )
    from_currency = forms.ModelChoiceField(
        queryset=Currency.objects.order_by("name"), required=True
    )
    to_currency = forms.ModelChoiceField(
        queryset=Currency.objects.order_by("name"),
        required=True,
    )
    result = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"readonly": "readonly"})
    )


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ("name", "type", "currency", "private")

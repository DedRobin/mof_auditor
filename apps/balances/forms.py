from django import forms
from django.conf import settings

from apps.balances.models import BalanceCurrency


class CurrencyConvertForm(forms.Form):
    from_amount = forms.DecimalField(
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
    )
    from_currency = forms.ModelChoiceField(
        queryset=BalanceCurrency.objects.order_by("name"),
        required=True
    )
    to_currency = forms.ModelChoiceField(
        queryset=BalanceCurrency.objects.order_by("name"),
        required=True
    )
    to_amount = forms.DecimalField(
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
    )

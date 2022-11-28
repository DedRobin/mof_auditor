from django import forms
from django.conf import settings

TRANSACTION_TYPE_CHOICE = (
    (None, "-----"),
    ("income", "Income"),
    ("expense", "Expense"),
)


class TransactionTypeFilterForm(forms.Form):
    cat_type = forms.ChoiceField(choices=TRANSACTION_TYPE_CHOICE, required=False)
    cat_name = forms.CharField(max_length=255, required=False)


class TransactionFilterForm(TransactionTypeFilterForm):
    balance = forms.CharField(max_length=255, required=False)
    from_amount = forms.DecimalField(
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        required=False,
    )
    to_amount = forms.DecimalField(
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        required=False,
    )
    comment = forms.CharField(max_length=255, required=False)
    from_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput)
    to_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput)

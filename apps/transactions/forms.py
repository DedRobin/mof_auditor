from django import forms
from django.conf import settings

TRANSACTION_TYPE_CHOICE = (
    (None, "-----"),
    ("income", "Income"),
    ("expense", "Expense"),
)


class TransactionTypeFilterForm(forms.Form):
    category__type = forms.ChoiceField(
        label="Category type", choices=TRANSACTION_TYPE_CHOICE, required=False
    )
    category__name = forms.CharField(
        label="Category name", max_length=255, required=False
    )


class TransactionFilterForm(TransactionTypeFilterForm):
    balance__name = forms.CharField(label="Balance", max_length=255, required=False)
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
    from_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "placeholder": "YYYY-MM-DD HH:MM",
            },
            format="%Y-%m-%d %H:%M",
        ),
    )
    to_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "placeholder": "YYYY-MM-DD HH:MM",
            },
            format="%Y-%m-%d %H:%M",
        ),
    )

from django import forms
from django.conf import settings

from apps.transactions.models import TransactionCategory

TRANSACTION_TYPE_CHOICE = (
    (None, "-----"),
    ("income", "Income"),
    ("expense", "Expense"),
)


# class TransactionTypeForm(forms.Form):
#     category__type = forms.ChoiceField(
#         label="Category type", choices=TRANSACTION_TYPE_CHOICE, required=False
#     )
#     category__name = forms.ChoiceField(
#         label="Category name", choices=TransactionCategory.objects.all(), required=False
#     )


class TransactionForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=TransactionCategory.objects.all(),
        required=False
    )
    amount = forms.DecimalField(
        max_digits=settings.MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        required=False,
    )
    comment = forms.CharField(max_length=255, required=False)


class TransactionFilterForm(forms.Form):
    category__type = forms.ChoiceField(
        label="Category type", choices=TRANSACTION_TYPE_CHOICE, required=False
    )
    category__name = forms.CharField(
        label="Category name", max_length=255, required=False
    )
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

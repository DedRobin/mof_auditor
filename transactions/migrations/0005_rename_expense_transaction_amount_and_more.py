# Generated by Django 4.1.1 on 2022-10-26 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0004_alter_transaction_expense_alter_transaction_income"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction",
            old_name="expense",
            new_name="amount",
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="income",
        ),
    ]
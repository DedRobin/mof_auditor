# Generated by Django 4.1.1 on 2022-12-14 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0003_alter_transaction_created_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transactioncategory",
            options={"verbose_name_plural": "Transaction Categories"},
        ),
    ]

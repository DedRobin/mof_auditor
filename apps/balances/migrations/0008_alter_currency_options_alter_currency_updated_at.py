# Generated by Django 4.1.1 on 2022-12-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("balances", "0007_rename_balancecurrency_currency"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="currency",
            options={"verbose_name_plural": "Currencies"},
        ),
        migrations.AlterField(
            model_name="currency",
            name="updated_at",
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]

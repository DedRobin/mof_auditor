# Generated by Django 4.1.1 on 2022-11-07 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0014_rename_users_group_invited_users"),
        ("balances", "0004_rename_for_groups_balance_groups"),
    ]

    operations = [
        migrations.AlterField(
            model_name="balance",
            name="groups",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="balances", to="groups.group"
            ),
        ),
    ]

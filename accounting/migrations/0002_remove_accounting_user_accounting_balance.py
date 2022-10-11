# Generated by Django 4.1.1 on 2022-10-11 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("balance", "0003_rename_user_balance_users"),
        ("accounting", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="accounting",
            name="user",
        ),
        migrations.AddField(
            model_name="accounting",
            name="balance",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="accounting",
                to="balance.balance",
            ),
        ),
    ]

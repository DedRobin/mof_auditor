# Generated by Django 4.1.1 on 2022-11-18 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0023_rename_users_permission_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="group",
            name="permissions",
        ),
        migrations.DeleteModel(
            name="Permission",
        ),
    ]

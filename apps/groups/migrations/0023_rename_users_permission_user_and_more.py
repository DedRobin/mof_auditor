# Generated by Django 4.1.1 on 2022-11-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0022_remove_permission_codename_remove_permission_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="permission",
            old_name="users",
            new_name="user",
        ),
        migrations.AlterField(
            model_name="permission",
            name="permission_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("read", "Read"),
                    ("create", "Create"),
                    ("update", "Update"),
                    ("delete", "Delete"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-18 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("permissions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="permissiontype",
            name="name",
            field=models.CharField(
                choices=[
                    ("read", "Read"),
                    ("create", "Create"),
                    ("update", "Update"),
                    ("delete", "Delete"),
                ],
                max_length=255,
                unique=True,
            ),
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            (None, "Empty"),
                            ("male", "Male"),
                            ("female", "Female"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]

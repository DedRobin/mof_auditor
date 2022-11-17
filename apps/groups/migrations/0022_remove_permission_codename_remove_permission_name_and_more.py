# Generated by Django 4.1.1 on 2022-11-17 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("groups", "0021_alter_invitation_pub_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="permission",
            name="codename",
        ),
        migrations.RemoveField(
            model_name="permission",
            name="name",
        ),
        migrations.AddField(
            model_name="permission",
            name="permission_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Read", "read"),
                    ("Create", "create"),
                    ("Update", "update"),
                    ("Delete", "delete"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.RemoveField(
            model_name="permission",
            name="users",
        ),
        migrations.AddField(
            model_name="permission",
            name="users",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="group_permissions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

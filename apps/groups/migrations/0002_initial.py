# Generated by Django 4.1.1 on 2022-11-22 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("groups", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="groupinformation",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="group_info",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="group_info",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="groups.groupinformation",
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="invited_users",
            field=models.ManyToManyField(
                blank=True, related_name="user_groups", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]

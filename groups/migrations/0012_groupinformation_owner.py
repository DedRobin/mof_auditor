# Generated by Django 4.1.1 on 2022-10-31 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0011_alter_group_permissions_alter_group_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupinformation',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_info', to=settings.AUTH_USER_MODEL),
        ),
    ]

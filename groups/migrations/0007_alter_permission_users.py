# Generated by Django 4.1.1 on 2022-10-24 17:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0006_alter_permission_codename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_rename_grouppermission_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='codename',
            field=models.CharField(default='read_only', max_length=255),
        ),
    ]

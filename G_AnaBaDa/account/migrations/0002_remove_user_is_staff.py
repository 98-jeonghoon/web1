# Generated by Django 4.1 on 2022-08-13 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="is_staff",),
    ]

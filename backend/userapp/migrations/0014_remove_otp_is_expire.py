# Generated by Django 5.0.6 on 2024-09-02 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0013_otp_is_expire"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="otp",
            name="is_expire",
        ),
    ]

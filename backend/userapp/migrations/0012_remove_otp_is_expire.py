# Generated by Django 5.0.6 on 2024-09-02 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0011_otp_is_expire"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="otp",
            name="is_expire",
        ),
    ]

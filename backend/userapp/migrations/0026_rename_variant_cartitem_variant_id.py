# Generated by Django 5.0.6 on 2024-09-10 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0025_alter_cartitem_variant"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartitem",
            old_name="variant",
            new_name="variant_id",
        ),
    ]

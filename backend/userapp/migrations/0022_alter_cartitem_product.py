# Generated by Django 5.0.6 on 2024-09-10 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0021_address_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="userapp.product",
                unique=True,
            ),
        ),
    ]

# Generated by Django 5.0.6 on 2024-09-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0017_product_created_date_product_in_stock_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="rating",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]

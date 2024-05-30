# Generated by Django 5.0.6 on 2024-05-28 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_address_remove_product_hours_and_more'),
        ('restaurant', '0005_remove_restaurant_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='restaurant.restaurant'),
        ),
    ]
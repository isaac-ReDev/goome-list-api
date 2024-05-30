# Generated by Django 5.0.6 on 2024-05-28 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_address_remove_product_hours_and_more'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='products',
            field=models.ManyToManyField(related_name='products', to='product.product'),
        ),
    ]
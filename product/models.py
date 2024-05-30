from django.db import models
from restaurant.models import Restaurant


CATEGORY_CHOICE = (
    ('DOCES', 'Doces'),
    ('SAlGADOS', 'Salgados'),
    ('SUCOS', 'Sucos'),
    ('REFRIGERANTES', 'Regrigerantes'),
    ('MASSAS', 'Massas'),
    ('Vegetariano', 'Vegetariano'),
)

class Product(models.Model):
    # photo = models.ImageField()
    name = models.CharField(max_length=200)
    # @classmethod
    # def get_default_pk()
    restaurant = models.ForeignKey(Restaurant, default=1 ,on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(default=0.00)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICE, null=True, blank=True)

    promotion = models.BooleanField(default=False)
    promotion_description = models.TextField(max_length=300, null=True, blank=True)
    promotion_price = models.FloatField(null=True, blank=True)
    promotion_date = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
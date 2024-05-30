from django.db import models
# from product.models import Product 

DAYS_CHOICE = (
        ('SEG-SEX', ' Segunda à Sexta das 09h as 18h'),
        ('SAB-DOM', 'Sabado à Domingo'),    
    )
HORARIOS_CHOICE = (
        ('09h-18h', '09h as 18h'),
        ('11h-20h', '11h as 20h'),    
    )

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    # photo = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=200)    
    working_days = models.CharField(max_length=200, choices=DAYS_CHOICE)
    hours        = models.CharField(max_length=100, choices=HORARIOS_CHOICE)    
    # products = models.ManyToOneRel(Product, related_name='products')
    # products = models.CharField(max_length=200, choices=Product)


    def __str__(self):
        return self.name


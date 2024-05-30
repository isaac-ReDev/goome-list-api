from django.contrib import admin
from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id','name', 'price', 'promotion', 
        'promotion_description', 'promotion_price', 'promotion_date',           
        )
    
    

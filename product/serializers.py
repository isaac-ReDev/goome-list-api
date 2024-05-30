from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Product
        # fields = ['id', 'name', 
        #           'restaurants', 'price', 
        #           'category', 'promition', 
        #           'promotion_description',
        #           'promotion_price',
        #           'promotion_date',
        #           'products',
        #         ]
        fields = '__all__'
    
from rest_framework import generics
from restaurant.serializers import RestaurantSerializer
from product.serializers import ProductSerializer
from restaurant.models import Restaurant
from product.models import Product

class RestaurantListView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantProductsListView(generics.ListAPIView):
    # queryset = Restaurant.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        # return Product.objects.filter()
        return Product.objects.filter(restaurant__id=id)
        # list = Product.objects.restaurant = id
        # print(list)
        
        # return {"id": id}
        
    

class RestaurantRetriaverUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer



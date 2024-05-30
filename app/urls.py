from django.contrib import admin
from django.urls import path
from restaurant.views import RestaurantListView, RestaurantProductsListView, RestaurantRetriaverUpdateDestroy
from product.views import ProductListVIerw, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-create-list-view'),
    path('restaurants-products/<int:pk>/', RestaurantProductsListView.as_view(), name="restaurant-product-list-view"),
    path('restaurants/<int:pk>/', RestaurantRetriaverUpdateDestroy.as_view(), name='restaurant-details-view'),

    path('products/', ProductListVIerw.as_view(), name='product-create-list-view'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-details-view'),

]

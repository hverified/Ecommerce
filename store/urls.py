from django.urls import path
from .views import (storeView, cartView, checkoutView,
                    updateItem, processOrder, productView)


urlpatterns = [
    path('', storeView, name="store"),
    path('cart/', cartView, name="cart"),
    path('checkout/', checkoutView, name="checkout"),
    path('update_item/', updateItem, name="update_item"),
    path('process_order/', processOrder, name="process_order"),
    path('product/<int:pid>', productView, name="product"),
]

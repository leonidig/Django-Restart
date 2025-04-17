
from django.urls import path
from .views import (index,
                    about,
                    product_details,
                    cart_detail_view,
                    cart_add,
                    remove_item_from_cart
                )

app_name = "products"



urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'), 
    path("product/<int:product_id>/", product_details, name="product_details"),
    path("cart_add/<int:product_id>/", cart_add, name="cart_add"),
    path("cart_details/", cart_detail_view, name="cart_detail"),
    path("cart_remove_item/<int:item_id>", remove_item_from_cart, name="remove_item")
]

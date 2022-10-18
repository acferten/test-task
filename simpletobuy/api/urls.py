from django.urls import path

from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name="products" ),
    path('cart/<int:pk>', CartApiView.as_view(), name="addtocart"),
    path('cart/', CartAPIList.as_view())
]

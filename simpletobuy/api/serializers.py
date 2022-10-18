from rest_framework import serializers

from .models import Product, Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    e = Product.objects.select_related('name', 'description').get(id=product)

    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity']

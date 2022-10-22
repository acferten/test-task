from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Product, Cart, AdvUser


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'product', 'name', 'description', 'price']


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=AdvUser.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = AdvUser
        fields = ['fio', 'email', 'password']

    def create(self, validated_data):
        user = AdvUser.objects.create(
            email=validated_data['email'],
            fio=validated_data['fio'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

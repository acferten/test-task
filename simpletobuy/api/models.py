from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def save(self, *args, **kwargs):
        self.username = self.email
        return super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=3000)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return object.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, default=1)

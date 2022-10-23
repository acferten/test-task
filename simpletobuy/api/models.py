from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver


class AdvUser(AbstractUser):
    fio = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fio']


class Product(models.Model):
    name = models.CharField(max_length=250, blank=False)
    description = models.CharField(max_length=3000, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE, null=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=3000)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    user = models.ForeignKey(AdvUser, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(AdvUser, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False)

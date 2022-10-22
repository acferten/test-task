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


# class Cart(models.Model):
#     user = models.ForeignKey(AdvUser, on_delete=models.CASCADE, null=True, blank=False)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
#     name = models.CharField(max_length=250)
#     description = models.CharField(max_length=3000)
#     price = models.DecimalField(max_digits=8, decimal_places=2)

    # quantity = models.IntegerField(null=False, default=1)

    # def __str__(self):
    #     return str(self.id)


class Order(models.Model):
    user = models.ForeignKey(AdvUser, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(AdvUser, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False)


class Cart(models.Model):
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.email) + " " + str(self.total_price)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username) + " " + str(self.product.product_name)


@receiver(pre_save, sender=CartItems)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    total_cart_items = CartItems.objects.filter(user=cart_items.user)
    cart = Cart.objects.get(id=cart_items.cart.id)
    cart.total_price = cart_items.price
    cart.save()
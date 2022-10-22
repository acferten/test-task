from django.contrib import admin

from .models import Product, AdvUser, Cart

admin.site.register(Product)
admin.site.register(AdvUser)
admin.site.register(Cart)

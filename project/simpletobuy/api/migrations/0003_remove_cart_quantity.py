# Generated by Django 4.1.2 on 2022-10-20 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_orderitem_price_cart_description_cart_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]

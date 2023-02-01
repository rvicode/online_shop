from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from products.models import Product


class Order(models.Model):
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    is_paid = models.BooleanField(default=False)

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    message = models.TextField()
    address = models.TextField()

    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Time Created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Time Updated'))

    def __str__(self):
        return (self.firstname + ' ' + self.lastname + ' ' )


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Time Created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Time Updated'))

    def __str__(self):
        return (self.firstname + ' ' + self.lastname + ' ' )

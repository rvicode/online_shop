from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=False)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model, on_delete=models.CASCADE, max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True, blank=True)
    description = models.TextField()
    active = models.BooleanField(default=True)

    datetime_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user, self.product

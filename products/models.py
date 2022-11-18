from django.db import models
from django.urls import reverse

from accounts.models import CustomUser


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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True, blank=True)
    description = models.TextField()
    active = models.BooleanField(default=True)

    datetime_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

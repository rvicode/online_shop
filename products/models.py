from django.db import models
from django.urls import reverse


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
    user = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user, self.title
    
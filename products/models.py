from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Name Product'))
    description = models.TextField(verbose_name=_('Description'))
    price = models.PositiveIntegerField(verbose_name=_('Product Price'))
    active = models.BooleanField(default=False, verbose_name=_('Its Active'))
    image = models.ImageField(verbose_name=_('Image'), upload_to='Product/img')

    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Time Created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Time Updated'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, max_length=50, related_name="comments",
                             verbose_name=_('Author'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments", verbose_name=_('Product'))
    description = models.TextField(verbose_name=_('Comment Text'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True, blank=True,
                               verbose_name=_('Reply comment'))
    active = models.BooleanField(default=True, verbose_name=_('Its Active'))

    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name=_('Time created'))

    # Manager
    objects = models.Manager()
    active_comment_manager = ActiveCommentsManager()

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product_id])

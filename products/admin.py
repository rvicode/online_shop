from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, TabularInlineJalaliMixin

from .models import Product, Comment


class CommentsInline(TabularInlineJalaliMixin, admin.TabularInline):
    model = Comment
    fields = ['user', 'description', 'active', 'datetime_create']
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active', ]
    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'description', 'active', 'datetime_create']

from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, TabularInlineJalaliMixin

from .models import Order, OrderItem


class CommentsInline(TabularInlineJalaliMixin, admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price']
    extra = 1


@admin.register(Order)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['username', 'address', 'is_paid', 'datetime_create']
    inlines = [
        CommentsInline,
    ]


@admin.register(OrderItem)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'datetime_create']

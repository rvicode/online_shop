from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['firstname','lastname','phonenumber','address','message']
        widgets = {
            "message": forms.Textarea(attrs={'rows': 4, 'placeholder':_('Please enter a message or leved in empty form')}),
            'address': forms.Textarea(attrs={'rows': 5}),
        }
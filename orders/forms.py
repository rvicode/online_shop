from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['firstname','lastname','phonenumber','message','address']
        widgets = {
            "message": forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 5})
        }
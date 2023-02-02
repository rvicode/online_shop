from django.shortcuts import render

from .forms import OrderForm


def order_create_view(request):
    form = OrderForm()
    return render(request, 'orders/order_create.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import OrderForm


@login_required
def order_create_view(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.username = request.user
            print(forms.username)
            forms.save()
            return redirect('product:product_list')

    return render(request, 'orders/order_create.html', {'form': form})

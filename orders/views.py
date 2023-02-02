from django.shortcuts import render, redirect

from .forms import OrderForm


def order_create_view(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('account_login')
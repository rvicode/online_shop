from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib import messages

from cart.forms import ProductCartForm
from .models import Product, Comment
from .forms import CommentForm


def messages_text(request):
    messages.success(request, 'This is a success message')
    messages.warning(request, 'This is a success message')
    messages.error(request, 'This is a success message')
    return render(request, 'products/massagestemplate.html')


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['add_to_cart_form'] = ProductCartForm()
        return context


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_comment_form'] = CommentForm()
        context['add_to_cart_form'] = ProductCartForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, pk=product_id)
        obj.product = product
        return super().form_valid(form)



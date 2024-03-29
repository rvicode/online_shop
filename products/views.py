from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import Product, Comment
from .forms import CommentForm


class ProductListView(generic.ListView):
    http_method_names = ['get']
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        return context


class ProductDetailView(generic.DetailView):
    http_method_names = ['get']
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    http_method_names = ['post']
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, pk=product_id)
        obj.product = product
        messages.success(self.request, _('Your comment was successfully!'))
        return super().form_valid(form)

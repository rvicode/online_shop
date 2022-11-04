from django.urls import reverse_lazy

from django.views import generic
from .forms import CustomUserCreationForm


class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    context_object_name = 'form'
    success_url = reverse_lazy('login')

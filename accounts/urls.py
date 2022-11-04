from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.SignUpPageView.as_view(), name='sign_up'),
]

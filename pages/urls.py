from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about_us/', views.AboutUsView.as_view(), name='about_us'),
]

"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import IndexListView, ItemDetailView, CartListView, AddCartView, remove_from_cart, PayCancelView, PaySuccessView, PayWithStripe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexListView.as_view()),
    path('items/<str:pk>/', ItemDetailView.as_view()),
    path('cart/', CartListView.as_view()),
    path('cart/add/', AddCartView.as_view()),
    path('cart/remove/<str:pk>/', remove_from_cart),
    path('pay/checkout/', PayWithStripe.as_view()),
    path('pay/success/', PaySuccessView.as_view()),
    path('pay/cancel/', PayCancelView.as_view()),
]

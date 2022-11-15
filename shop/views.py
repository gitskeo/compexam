from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)
from django.urls import reverse_lazy
from .models import *


class HomePageView(TemplateView):
    template_name = "home.html"


class CartView(ListView):
    model = OrderItem
    context = {'order': model}
    template_name = "cart.html"


class CheckoutView(ListView):
    template_name = "checkout.html"
    model = ShippingAddress
    context = {'shippingaddress': model}
    success_url = reverse_lazy("home")


class StoreView(ListView):
    model = Product
    context = {'products': model}
    template_name = "store.html"

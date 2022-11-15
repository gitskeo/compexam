from django.urls import path
from .views import HomePageView, CartView, CheckoutView, StoreView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("cart/", CartView.as_view(), name="cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("store/", StoreView.as_view(), name="store"),
]

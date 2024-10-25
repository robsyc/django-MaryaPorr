from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse

import stripe

from django.views.generic import ListView, DetailView
from .models import Product


def home(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == "POST":
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": "price_1Q9Mmz06AuYbLRJ64JETB3nA",  # enter yours here!!!
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=request.build_absolute_uri(reverse("success")),
            cancel_url=request.build_absolute_uri(reverse("cancel")),
        )
        return redirect(checkout_session.url, code=303)
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def success(request):
    return render(request, "success.html")

def cancel(request):
    return render(request, "cancel.html")

def products(request):
    return render(request, "products.html")

class ProductListView(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
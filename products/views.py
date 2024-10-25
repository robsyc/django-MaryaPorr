from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def success(request):
    return render(request, "success.html")

def cancel(request):
    return render(request, "cancel.html")

def products(request):
    return render(request, "products.html")

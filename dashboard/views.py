from django.shortcuts import render
from core import models


def index(request):
    return render(request, "dashboard/index.html", {})


def orders(request):
    return render(request, "dashboard/orders.html", {})


def products(request):
    product_list = models.Widget.objects.all()
    return render(request, "dashboard/products.html", {"widget_list": product_list})

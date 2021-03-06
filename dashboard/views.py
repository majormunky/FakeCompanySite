from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from core import models
from core.api import serializers


@login_required
def index(request):
    widget_data = serializers.WidgetSerializer(
        models.Widget.objects.all(), many=True
    ).data
    return render(request, "dashboard/index.html", {"widget_data": widget_data})


@login_required
def orders(request):
    return render(request, "dashboard/orders.html", {})


@login_required
def widgets(request):
    widget_list = models.Widget.objects.all()
    return render(request, "dashboard/widgets.html", {"widget_list": widget_list})


@login_required
def widget_detail(request, pk):
    widget_data = get_object_or_404(models.Widget, pk=pk)
    return render(request, "dashboard/widget_detail.html", {"widget_data": widget_data})


@login_required
def customers(request):
    customer_list = get_user_model().objects.filter(groups__name="Customer")
    return render(request, "dashboard/customers.html", {"customer_list": customer_list})


@login_required
def customer_detail(request, pk):
    customer_data = get_object_or_404(get_user_model(), pk=pk)
    return render(
        request, "dashboard/customer_detail.html", {"customer_data": customer_data}
    )

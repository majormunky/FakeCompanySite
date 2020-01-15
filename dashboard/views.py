from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core import models


@login_required
def index(request):
    return render(request, "dashboard/index.html", {})


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

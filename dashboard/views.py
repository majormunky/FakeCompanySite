from django.shortcuts import render


def index(request):
	return render(request, "dashboard/index.html", {})


def orders(request):
	return render(request, "dashboard/orders.html", {})

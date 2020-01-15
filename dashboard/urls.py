from django.urls import path
from dashboard import views


urlpatterns = [
    path("", views.index),
    path("orders/", views.orders),
    path("products/", views.products),
    path("widgets/<int:pk>/", views.widget_detail),
]

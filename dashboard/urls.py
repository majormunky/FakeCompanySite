from django.urls import path
from dashboard import views


urlpatterns = [
    path("", views.index),
    path("orders/", views.orders),
    path("widgets/", views.widgets),
    path("widgets/<int:pk>/", views.widget_detail),
    path("customers/", views.customers),
]

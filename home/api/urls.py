from django.urls import path
from .views import OdooProxyView

urlpatterns = [
    path("odoo/", OdooProxyView.as_view(), name="odoo-products"),
]

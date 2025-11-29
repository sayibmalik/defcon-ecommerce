from django.urls import path, include

from home.api.views import DynamicModelAPIView, OdooProxyView
from .views import *

urlpatterns = [
    path("proxy/", OdooProxyView.as_view(), name="odoo-products"),
    path("models/", DynamicModelAPIView.as_view(), name="dynamic-models"),
]

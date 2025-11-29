from django.urls import path, include

from home.api.views import DynamicModelView, OdooProxyView
from .views import *

urlpatterns = [
    path("proxy/", OdooProxyView.as_view(), name="odoo-products"),
    path("models/", DynamicModelView.as_view(), name="dynamic-models"),
]

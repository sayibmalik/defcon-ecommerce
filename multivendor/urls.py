# multivendor/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, VendorViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]


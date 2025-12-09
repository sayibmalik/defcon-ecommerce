# multivendor/views.py
from rest_framework import viewsets, permissions, filters as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Vendor
from .serializers import ProductSerializer, VendorSerializer
from .permissions import IsVendorOwnerOrReadOnly
from .filters import VendorFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters import rest_framework as filters

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all().select_related("user", "res_user")
    serializer_class = VendorSerializer
    permission_classes = [IsVendorOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, drf_filters.OrderingFilter, drf_filters.SearchFilter]
    filterset_class = VendorFilter
    ordering_fields = ["created_on", "rating", "name"]
    search_fields = ["name", "description", "slug"]

    def perform_create(self, serializer):
        # default owner to request.user if not provided
        user = getattr(self.request.user, "pk", None)
        if user and not serializer.validated_data.get("user"):
            serializer.save(user=self.request.user)
        else:
            serializer.save()

class ProductFilter(filters.FilterSet):
    vendor = filters.NumberFilter(field_name="vendor",lookup_expr='exact') 

    class Meta:
        model = Product
        fields = ['vendor']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = ProductFilter 

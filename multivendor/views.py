# multivendor/views.py
from rest_framework import viewsets, permissions, filters as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Vendor, Product
from .serializers import VendorSerializer, ProductSerializer
from .permissions import IsVendorOwnerOrReadOnly
from .filters import VendorFilter, ProductFilter


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


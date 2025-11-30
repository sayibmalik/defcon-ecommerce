# multivendor/filters.py
import django_filters
from .models import Vendor


class VendorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    is_active = django_filters.BooleanFilter(field_name="is_active")
    user = django_filters.NumberFilter(field_name="user__id")
    res_user = django_filters.NumberFilter(field_name="res_user__id")

    class Meta:
        model = Vendor
        fields = ["name", "is_active", "user", "res_user"]


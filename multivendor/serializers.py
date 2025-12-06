from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product, Vendor, VendorBankDetail
from home.models import ProductTemplate
# Import ResUsers appropriately
from home.models import ResUsers
from decimal import Decimal, InvalidOperation

class SafeDecimalField(serializers.DecimalField):
    def to_representation(self, value):
        try:
            return super().to_representation(value)
        except (InvalidOperation, ValueError, TypeError):
            return None  # or "0.00" if you prefer
        
User = get_user_model()




class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email",)


class ResUsersShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResUsers
        # include fields you want exposed; adjust as necessary
        fields = ("id", "name", "phone")



class VendorBankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorBankDetail
        fields = ("bank_name", "account_number", "iban")


class VendorSerializer(serializers.ModelSerializer):
    # Two keys requested:
    user = UserShortSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source="user")

    res_user = ResUsersShortSerializer(read_only=True)
    res_user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=ResUsers.objects.all(), source="res_user", required=False, allow_null=True)


    class Meta:
        model = Vendor
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "is_active",
            "created_on",
            "updated_on",
            "storefront_url",
            "rating",
            # the two keys:
            "user",
            "user_id",
            "res_user",
            "res_user_id",
            "bank_detail",
        )
        read_only_fields = ("id", "created_on", "updated_on", "rating")


class ProductTemplateSerializer(serializers.ModelSerializer):
    price = SafeDecimalField(max_digits=10, decimal_places=2, required=False)
    list_price = SafeDecimalField(max_digits=10, decimal_places=2, required=False)
    volume = SafeDecimalField(max_digits=10, decimal_places=2, required=False)
    weight = SafeDecimalField(max_digits=10, decimal_places=2, required=False)
    compare_list_price = SafeDecimalField(max_digits=10, decimal_places=2, required=False)
    
    class Meta:
        model = ProductTemplate
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    name = ProductTemplateSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'


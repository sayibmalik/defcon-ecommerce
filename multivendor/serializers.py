from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Vendor, Product, VendorBankDetail

# Import ResUsers appropriately
from home.models import ResUsers

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

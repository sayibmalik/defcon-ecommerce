from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Sum
from .models import Product, Vendor, VendorBankDetail
from home.models import ProductTemplate, ProductImage, StockQuant
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


class ProductImageSerializer(serializers.ModelSerializer):
    """Serializer for 128px product images"""
    class Meta:
        model = ProductImage
        fields = ('id', 'name', 'image_1128')


class ProductSerializer(serializers.ModelSerializer):
    name = ProductTemplateSerializer(read_only=True)
    image_128 = serializers.SerializerMethodField(read_only=True)
    quantity = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = ('id', 'vendor', 'name', 'image_128', 'quantity')
    
    def get_image_128(self, obj):
        """
        Retrieve the 128px image for the product.
        Returns the image_1128 field from ProductImage model if available.
        """
        try:
            product_images = ProductImage.objects.filter(
                product_tmpl_id=obj.name.id
            ).first()
            
            if product_images and product_images.image_1128:
                return {
                    'id': product_images.id,
                    'name': product_images.name,
                    'image_128': product_images.image_1128
                }
        except Exception as e:
            return None
        return None
    
    def get_quantity(self, obj):
        """
        Retrieve total quantity available for the product from StockQuant.
        Sums up quantity available across all warehouses.
        """
        try:
            total_quantity = StockQuant.objects.filter(
                product_id=obj.name.id
            ).aggregate(
                total_qty=Sum('quantity')
            )['total_qty'] or 0
            
            return float(total_quantity)
        except Exception as e:
            return 0


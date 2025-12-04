# multivendor/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone
from home.models import ResUsers, ProductTemplate

# Adjust this import to where your ResUsers model actually lives
from home.models import ResUsers


class Vendor(models.Model):
    """
    Main vendor model.
    Has two "keys" requested:
      - user: standard Django auth User (owner/account manager)
      - res_user: the existing ResUsers model instance
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="vendors",
        help_text="Django auth user who manages this vendor"
    )
    res_user = models.ForeignKey(
        ResUsers,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="vendors",
        help_text="Reference to existing ResUsers entry (if any)"
    )

    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    # Optional: vendor related settings
    storefront_url = models.URLField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"
        ordering = ["-created_on"]

    # def __str__(self):
    #     return self.res_user
    def __str__(self):
        # return "{}".format(self.res_user.login)
        return f"{self.res_user.login} {self.user.username} - {self.user.email}"



class VendorBankDetail(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name="bank_detail")
    bank_name = models.CharField(max_length=255, blank=True)
    account_number = models.CharField(max_length=100, blank=True)
    iban = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"Bank detail for {self.vendor.name}"


class Product(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.PROTECT,
        related_name="vendor"
    )
    name = models.ForeignKey(
        ProductTemplate,
        on_delete=models.PROTECT,
        related_name="products"
    )
    def __str__(self):
        return f" {self.name.name}"
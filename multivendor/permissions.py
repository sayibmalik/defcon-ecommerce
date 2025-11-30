from rest_framework import permissions


class IsVendorOwnerOrReadOnly(permissions.BasePermission):
    """
    Write permissions are allowed only to the user who owns the Vendor (Vendor.user) or staff.
    Read allowed to everyone.
    """

    def has_permission(self, request, view):
        # Allow list and retrieve for any user (optionally adjust).
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # staff can edit anything
        if request.user.is_staff:
            return True
        return obj.user == request.user


import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JsonRPCSerializer, create_dynamic_serializer
from django.apps import apps
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.text import slugify

# local models
from multivendor.models import Vendor
from home.models import ResUsers as ResUsersModel


class RegisterUserAPIView(APIView):
    """
    Django API that accepts the exact JSON format and calls Odoo JSON-RPC.
    """
    def post(self, request):
        serializer = JsonRPCSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payload = serializer.validated_data
        
        # Extract params
        name = payload["name"]
        email = payload["email"]
        password = payload["password"]

        # db = args[0]
        db = "zainab"
        # uid = args[1]
        uid = 2
      
        odoo_url = os.environ.get('ODOO_URL', 'http://192.168.1.2:8099/jsonrpc/')

        # Prepare JSON-RPC data for Odoo call
        odoo_payload ={
  "jsonrpc": "2.0",
  "method": "call",
  "params": {
    "service": "object",
    "method": "execute_kw",
    "args": [
      db,
      uid,
      "Defcon@123#",
      "res.users",
      "create",
      [
        {
          "name": name,
          "login": email,
          "email": email,
          "password": password,
          "sel_groups_1_10_11": 10,
          "active": True,
          "share": True
        }
      ]
    ]
  },
  "id": 1
}
        try:
          response = requests.post(odoo_url, json=odoo_payload)
          odoo_result = response.json()
        except Exception as e:
          return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # If Odoo returned an error, forward it
        if isinstance(odoo_result, dict) and odoo_result.get("error"):
          return Response(odoo_result, status=status.HTTP_400_BAD_REQUEST)

        # Create local Django user and Vendor entry after successful remote create
        try:
          User = get_user_model()
          username = email or getattr(User, 'USERNAME_FIELD', None) or email

          with transaction.atomic():
            # Avoid duplicate Django users
            django_user = User.objects.filter(email=email).first()
            created_user = False
            if not django_user:
              # create_user should handle password hashing
              try:
                django_user = User.objects.create_user(username=email, email=email, password=password)
              except TypeError:
                # fallback if custom user model expects different args
                django_user = User.objects.create(email=email)
                django_user.set_password(password)
                django_user.save()
              created_user = True

            # Try to find corresponding ResUsers record in local DB
            res_user = ResUsersModel.objects.filter(login=email).first()

            # Build a slug for vendor; ensure uniqueness
            base_slug = slugify(email.split("@")[0]) or slugify(name) or "vendor"
            slug = base_slug
            counter = 1
            while Vendor.objects.filter(slug=slug).exists():
              slug = f"{base_slug}-{counter}"
              counter += 1

            vendor = Vendor.objects.create(user=django_user, res_user=res_user, slug=slug)

        except Exception as e:
          # Return Odoo result but include local creation failure note
          return Response({"odoo": odoo_result, "local_error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"odoo": odoo_result, "user_created": created_user, "vendor_id": vendor.id})


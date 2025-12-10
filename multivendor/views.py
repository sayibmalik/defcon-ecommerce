# multivendor/views.py
from home.models import SaleOrder
from rest_framework import viewsets, permissions, filters as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Vendor
from .serializers import ProductSerializer, VendorSerializer
from .permissions import IsVendorOwnerOrReadOnly
from .filters import VendorFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters import rest_framework as filters
from rest_framework.response import Response
from .models import EmailOTPVerification
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
import random
from django.core.mail import send_mail
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.db import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken


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


class SaleOrderFilter(filters.FilterSet):
    vendor = filters.NumberFilter(field_name="vendor",lookup_expr='exact') 

    class Meta:
        model = SaleOrder
        fields = ['vendor']


class SaleOrderViewSet(viewsets.ModelViewSet):
    queryset = SaleOrder.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = SaleOrderFilter 


class check_auth(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        res={
            "username": request.user.username,
            "userid": request.user.id,
            "full_name": request.user.first_name + " " + request.user.last_name,
        }
        return Response(res)
    

class RegisterCompanyView(APIView):
    permission_classes = [AllowAny]

    def generate_otp(self):
        return str(random.randint(100000, 999999))

    def send_otp_email(self, email, otp):
        subject = "Defcon ERP - Verify your email"
        message = f"Your OTP for verifying your account is {otp}"
        send_mail(subject, message, 'ubaid@defconinnovations.com', [email])

    def create_user_for_company(self, company_name, data):
        role_id = 1  # Assuming 1 is Admin or Owner role
        password = data.get('password')
        company = Vendor.objects.create(OrganizationType = "Company", OrganizationName = company_name, Street1 = "NA", Street2 = "NA", Country = "NA", City = "NA", State = "NA", Zip = "NA", Phone = "NA", Mobile = "NA", Email = data.get('email'), Website = "NA", Taxid = "NA", CompanyRegistry = "NA", Currency = "NA", Logo = "NA", Ref = data.get('email'), is_archive = "False")

        user = User.objects.create(
            username=data.get('username'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            password=make_password(password),
            is_active=False,
        )
       
        # try:

        #     group = Group.objects.get(name="Admin")  # Change group name as needed
        #     user.groups.add(group)

        #     group = Group.objects.get(name="CRM")  # Change group name as needed
        #     user.groups.add(group)

        # except Group.DoesNotExist:
        #     pass  # Optional: handle or log missing group

        return user
    

    def post(self, request):
        company_name = request.data.get('company_name')
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        if not all([company_name, email, username, password, confirm_password, first_name, last_name]):
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if password != confirm_password:
            return Response({"error": "Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            

            # Create user for company
            user = self.create_user_for_company(company_name, request.data)
            
            

            # Generate OTP
            otp = self.generate_otp()
            EmailOTPVerification.objects.create(user=user, otp=otp)

            # Send OTP email
            self.send_otp_email(email, otp)

            return Response({"message": "Company and user created. OTP sent to email."}, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response({"error": "Username or email already exists."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        if not all([email, otp]):
            return Response({"error": "Email and OTP are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            otp_record = EmailOTPVerification.objects.filter(user=user, otp=otp, is_verified=False).last()

            if not otp_record:
                return Response({"error": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)

            # Mark OTP as used
            otp_record.is_verified = True
            otp_record.save()

            # Activate user
            user.is_active = True
            user.save()

            return Response({"message": "OTP verified. Account activated."}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class LogoutView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        try:
            token = request.COOKIES.get('refreshToken')
            refresh_token = RefreshToken(token)
            refresh_token.blacklist()
            return Response({'message': 'Logout successful'})
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        
from django.contrib.auth import authenticate, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from .models import Enquiry,OnlineEnquiry,ContactEnquiry,Admission
from .serializer import EnquirySerializer, ContactEnquirySerializer,AdmissionSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import OnlineEnquirySerializer
from rest_framework.viewsets import ModelViewSet

@api_view(['POST'])
def admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'success': True,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'username': user.username
        })
    else:
        return Response({

            'success': False,
            'message': 'Invalid username or password'
        }, status=status.HTTP_401_UNAUTHORIZED)
@api_view(["POST"])
def create_admin_once(request):
    try:
        if User.objects.filter(username="admin").exists():
            return Response(
                {"message": "Admin already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        User.objects.create_superuser(
            username="admin",
            email="info@7itechsolutions.com",
            password="7itech@7"
        )

        return Response(
            {"message": "Admin created successfully"},
            status=status.HTTP_201_CREATED
        )

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = Enquiry.objects.all().order_by("-created_at")
    serializer_class = EnquirySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "count": queryset.count(),
            "data": serializer.data
        })

class OnlineEnquiryViewSet(ModelViewSet):
    queryset = OnlineEnquiry.objects.all().order_by("-created_at")
    serializer_class = OnlineEnquirySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "count": queryset.count(),
            "results": serializer.data
        })

    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Enquiry submitted successfully",
                
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "success": False,
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class ContactEnquiryViewSet(viewsets.ModelViewSet):
    queryset = ContactEnquiry.objects.all().order_by("-created_at")
    serializer_class = ContactEnquirySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "count": queryset.count(),
            "results": serializer.data
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Enquiry submitted successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "success": False,
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def admin_logout(request):
    return Response({
        "success": True,
        "message": "Logged out successfully"
    })


class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all().order_by("-created_at")
    serializer_class = AdmissionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "count": queryset.count(),
            "data": serializer.data
        })

# @api_view(["GET", "POST"])
# def admission_view(request):
#     if request.method == "GET":
#         admissions = Admission.objects.all()
#         serializer = AdmissionSerializer(admissions, many=True)
#         return Response(
#             {"count": admissions.count(), "data": serializer.data},
#             status=200
#         )

#     if request.method == "POST":
#         serializer = AdmissionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)

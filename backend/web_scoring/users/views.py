from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import UserSerializer


class JWTTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


from django.views import generic
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from .serializers import (
    MyTokenObtainPairSerializer,
    CreateUserSerializer,
    UserLabelSerializer,
    UserSerializer,
    UserLabelSerializer
)

class ObtainTokenPairWithPointsView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLabel(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserLabelSerializer

class CurrentUserView(APIView):
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            print(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegister(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.AllowAny]


class UserLogin(generics.CreateAPIView):
  permission_classes = [permissions.AllowAny]
  serializer_class = UserLoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'detail': 'Invalid credentials'}, status=401)

    refresh = RefreshToken.for_user(user)

    return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'id': user.id, 'username': user.username})
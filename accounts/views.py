from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')

    if not username or not password:
        return Response(
            {'error': 'Username and password are required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'Username already exists'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )

    token, created = Token.objects.get_or_create(user=user)

    return Response(
        {
            'message': 'User registered successfully',
            'username': user.username,
            'token': token.key
        },
        status=status.HTTP_201_CREATED
    )


class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            'token': response.data['token'],
            'message': 'Login successful'
        })


@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()

    return Response({
        'message': 'Logout successful'
    })

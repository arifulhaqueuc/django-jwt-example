from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    bio = request.data.get('bio', '')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(username=username)
    user.set_password(password)
    user.save()

    UserProfile.objects.create(user=user, bio=bio)

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    return Response({'message': 'User registered successfully.', 'token': token}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    return Response({'message': 'This is a protected view.', 'bio': user_profile.bio})

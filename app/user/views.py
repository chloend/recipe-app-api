"""
Views for the user API
"""
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
    )


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for a user"""
    serializer_class = AuthTokenSerializer

    # Define the renderer classes used to format the response.
    # This ensures that the response format is consistent with the rest
    # of the API, using the default rendering settings configured in
    # the API settings.
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

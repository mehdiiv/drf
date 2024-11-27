from rest_framework import viewsets, status
from rest_framework.response import Response

from api.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

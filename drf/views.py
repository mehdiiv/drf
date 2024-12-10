from rest_framework import viewsets, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView
from api.models import User, Message
from .serializers import UserSerializer, MessageSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class LimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    default_offset = 0
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 50

class UserViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin ,GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination

class MessageViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin ,GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

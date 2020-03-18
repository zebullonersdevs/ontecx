from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework import  generics
from .serializers import UserSerializer

User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User
    serializer_class = UserSerializer




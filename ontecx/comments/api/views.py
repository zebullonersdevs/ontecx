from django.db.models import F

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from ..models import (

   Comments
)
from .serializers import CommentSerializer
from .permission import IsOwner


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comments
    permission_classes = (IsAuthenticated,)

class DeleteCommentAPIView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comments
    permission_classes = (IsAuthenticated, IsOwner)
    lookup_url_kwarg = "id"



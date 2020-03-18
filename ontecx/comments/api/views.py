from django.db.models import F
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from ..models import Comments, RepliedComment

from .permission import IsOwner, IsRepliedOwner
from .serializers import CommentSerializer, RepliedCommentSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comments
    permission_classes = (IsAuthenticated,)


class RepliedCommentCreateAPIView(generics.CreateAPIView):
    serializer_class = RepliedCommentSerializer
    queryset = RepliedComment
    permission_classes = (IsAuthenticated,)

class DeleteRepliedCommentAPIView(generics.DestroyAPIView):
    serializer_class = RepliedCommentSerializer
    queryset = RepliedComment
    permission_classes = (IsAuthenticated, IsRepliedOwner)
    lookup_url_kwarg = "id"

class DeleteCommentAPIView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comments
    permission_classes = (IsAuthenticated, IsOwner)
    lookup_url_kwarg = "id"

from django.urls import path

from comments.api import views as article_comment_views

urlpatterns = [
   path("comment/", article_comment_views.CommentCreateAPIView.as_view(), name="create_comment"),
   path("delete-comment/<int:id>", article_comment_views.DeleteCommentAPIView.as_view(), name="delete_comment")
]

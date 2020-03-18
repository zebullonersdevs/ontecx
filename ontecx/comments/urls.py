from django.urls import path

from comments.api import views as article_comment_views

urlpatterns = [
   path("comment/", article_comment_views.CommentCreateAPIView.as_view(), name="create_comment"),
   path("delete-comment/<int:id>", article_comment_views.DeleteCommentAPIView.as_view(), name="delete_comment"),
   path("reply/", article_comment_views.RepliedCommentCreateAPIView.as_view(), name='create_reply'),
   path("delete-reply/<int:id>/", article_comment_views.DeleteRepliedCommentAPIView.as_view(), name="delete_reply")
]

from rest_framework import serializers

from ..models import Comments, RepliedComment

class RepliedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepliedComment
        fields = "__all__"

    def to_representation(self, instance):
        ret = super(RepliedCommentSerializer, self).to_representation(instance)
        ret["replied_by_name"] = instance.replied_by.username
        ret["replied_by_avatar"] = instance.replied_by.avatar
        return ret


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


    def to_representation(self, instance):
        ret = super(CommentSerializer, self).to_representation(instance)
        ret["commented_by_name"] = instance.comment_by.username
        ret["comment_by_avatar"] = instance.comment_by.avatar
        replies_instances = RepliedComment.objects.filter(replied_on=instance.pk).all()
        replies = RepliedCommentSerializer(instance=replies_instances, many=True).data
        ret["replies"] = replies
        return ret




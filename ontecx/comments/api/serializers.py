from rest_framework import serializers

from ..models import Comments

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


    def to_representation(self, instance):
        ret = super(CommentSerializer, self).to_representation(instance)
        ret["commented_by_name"] = instance.comment_by.username
        ret["comment_by_avatar"] = instance.comment_by.avatar
        return ret




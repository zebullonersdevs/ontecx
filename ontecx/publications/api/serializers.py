from rest_framework import serializers

from ..models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    publisher = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Publication
        fields = ("title", "content", "publication_category", "date_created", "publisher", "image_url")

    def get_publisher(self, instance):
        return instance.published_by.username

    def get_image_url(self, instance):
        return instance.image.url


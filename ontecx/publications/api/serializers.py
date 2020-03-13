from rest_framework import serializers

from comments.api.serializers import CommentSerializer

from ..models import Publication, PublicationCategory


class PublicationSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    uploaded_at = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    category_id = serializers.SerializerMethodField()
    comments  = CommentSerializer(required=False, many=True)
    class Meta:
        model = Publication
        fields = ("id", "title", "content",  "uploaded_at", "image_url", "category_name", "comments", "category_id")

    def get_image_url(self, instance):
        return instance.image

    def get_uploaded_at(self, instance):
        return instance.date_created

    def get_category_name(self, instance):
        return instance.publication_category.category

    def get_category_id(self, instance):
        return str(instance.publication_category.pk)


class PublicationCreateSerializer(serializers.ModelSerializer):
    feeds = PublicationSerializer(required=True, many=True)

    class Meta:
        fields = ("id", "category", "feeds")
        model = PublicationCategory


    def create(self, validated_data):
        feeds = validated_data.pop("feeds")
        user = self.context['request'].user
        feed_type = self.context['request'].query_params.get("feed_type")
        publication_category = PublicationCategory.objects.create(published_by=user, **validated_data)
        for feed in feeds:
            publication = Publication.objects.create(publication_category=publication_category, **feed)
            if feed_type == "SPONSORED":
                publication.sponsored_publication = publication
                publication.save()

            elif feed_type == "FEATURED":
                publication.featured_publication = publication
                publication.save()


            else:
                pass

        return publication_category

    def update(self, instance, validated_data):
        pass

    def to_representation(self, instance):
        publication = Publication.objects.get(publication_category=instance.pk)
        data = {
            "id": instance.pk,
            "category": instance.category,
            "publisher": instance.published_by.username,
            "feeds": PublicationSerializer(instance=publication).data
        }
        return data

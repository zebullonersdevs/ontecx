from django.db.models import F

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from ..models import (

    Publication,
    PublicationCategory,

)
from .serializers import PublicationCreateSerializer, PublicationSerializer


class PublicationListAPIView(generics.ListAPIView):
    queryset  = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_queryset(self):
        return self.queryset.order_by("-date_created")


class PublicationFilterAPIView(generics.ListAPIView):
    queryset  = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_queryset(self):
        filter_by= self.kwargs['category']
        return self.queryset.filter(publication_category__category=filter_by).all()


class PublicationDetailAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication
    serializer_class = PublicationSerializer
    lookup_url_kwargs = "pk"

class SponsoredPublicationListAPIView(generics.ListAPIView):
    queryset  = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_queryset(self):
        return self.queryset.filter(sponsored_publication=F("pk")).order_by('-date_created')

class FeaturedPublicationListAPIView(generics.ListAPIView):
    queryset  = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_queryset(self):
        return self.queryset.filter(featured_publication=F("pk")).order_by('-date_created')

class PublicationUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PublicationSerializer
    queryset = Publication
    permission_classes = (IsAdminUser, IsAuthenticated)
    lookup_url_kwarg = 'id'

class  PublicationCreateAPIView(generics.CreateAPIView):
    """ when creating feeds you will to specify if the
    type of feed to be a sponsored feed or a featured feed
    by passing feed_type as a query params to the endpoint url,
    query params key -- feed_type
    query_params value -- SPONSORED/FEATURED
    """
    serializer_class = PublicationCreateSerializer
    queryset = PublicationCategory
    permission_classes = (IsAdminUser, IsAuthenticated)

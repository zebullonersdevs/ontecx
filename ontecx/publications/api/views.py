from rest_framework import  generics

from ..models import Publication

from .serializers import PublicationSerializer

class PublicationListAPIView(generics.ListAPIView):
    queryset  = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_queryset(self):
        try:
            query = Publication.objects.latest()
        except Publication.DoesNotExist:
            return self.queryset.order_by("-date_created")
        return query

class PublicationDetailAPIVIew(generics.RetrieveAPIView):
    queryset = Publication
    serializer_class = PublicationSerializer
    lookup_url_kwargs = "id"


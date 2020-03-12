from rest_framework import generics, status
from rest_framework.response import Response

from ..models import DeviceID
from .serializers import NotificationSerializer


class NotificationEnableAPIView(generics.CreateAPIView):
    """Endpoint resource to enable notification for devices"""
    queryset = DeviceID
    serializer_class = NotificationSerializer


class NotificationDisableAPIView(generics.GenericAPIView):
    """ Endpoint resource to disable notification for devices """
    serializer_class= None

    def get(self, request, *args, **kwargs):
        try:
            device_id = kwargs['registration_id']
        except KeyError:
            return Response({"message": "registration_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            DeviceID.objects.filter(registered_id=kwargs['registration_id']).update(active=False)
            return Response({"message": "Device disabled"}, status=status.HTTP_200_OK)


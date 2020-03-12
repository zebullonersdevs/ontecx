from rest_framework import serializers

from ..models import DeviceID

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceID
        fields = ('registration_id',)


    def validate_registration_id(self, data):
        if DeviceID.objects.filter(registraion_id=data).exists():
            raise serializers.ValidationError('device already registered')
        return data

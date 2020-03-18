from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

def create_user(validated_data):
    user = User.objects.create_user(**validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user

class UserSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["username",  "name", "tokens", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def get_tokens(self, instance):
        refresh = RefreshToken.for_user(instance)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            }

    def create(self, validated_data):
        return create_user(validated_data)

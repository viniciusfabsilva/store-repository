from .models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    birth_date = serializers.DateField()

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user

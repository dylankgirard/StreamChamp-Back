from rest_framework import serializers
from .models import User, Stream


class StreamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stream
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):

    favorites = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'bio', 'favorites')

    # def create(self, validated_data):
    #     favorites, _ = Stream.objects.get_or_create(
    #         name=validated_data.get('stream').get('name'))
    #     return User.objects.create(name=validated_data.get('name'), stream=stream)

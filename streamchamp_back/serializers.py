from rest_framework import serializers
from .models import User, Stream

class UserSerializer(serializers.ModelSerializer):
    # users = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = User
        fields = ('id', 'name', 'bio', 'favorites')

class StreamSerializer(serializers.ModelSerializer):
    # streams = serializers.HyperlinkedRelatedField(
    #     view_name='stream_detail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = Stream
        fields = ('id', 'name', 'favorited')
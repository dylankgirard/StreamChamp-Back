from rest_framework import serializers
from .models import User, Stream

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'name', 'bio', 'favorites')

class StreamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stream
        fields = ('id', 'name')
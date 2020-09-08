from rest_framework import generics
from .serializers import UserSerializer, StreamSerializer
from .models import User, Stream

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StreamList(generics.ListCreateAPIView):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer

class StreamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
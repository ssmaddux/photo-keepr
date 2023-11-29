# views.py

from rest_framework import generics
from .serializers import UserSerializer, PhotoSerializer, PeopleSerializer
from .models import User, Photo, People

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PeopleList(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

class PeopleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


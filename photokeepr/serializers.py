from rest_framework import serializers
from .models import User, Photo, People

class UserSerializer(serializers.HyperlinkedModelSerializer):



    class Meta:
       model = User
       fields = ('id', 'name', 'email', 'phone', 'password')






class PhotoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    


 


    class Meta:
       model = Photo
       fields = ('id', 'date', 'photo_name', 'preview_url', 'image','comment','user')




class PeopleSerializer(serializers.ModelSerializer):
 


    class Meta:
       model = People
       fields = ('id', 'related_photo', 'related_user')










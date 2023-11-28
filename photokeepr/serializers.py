from rest_framework import serializers
from .models import User, Photo, People, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):



    class Meta:
       model = User
       fields = ('id', 'name', 'email', 'phone', 'password')

class CommentSerializer(serializers.ModelSerializer):
 


    class Meta:
       model = Comment
       fields = ('id', 'related_picture', 'comment')




class PhotoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    


 


    class Meta:
       model = Photo
       fields = ('id', 'date', 'photo_name', 'preview_url', 'image','user')




class PeopleSerializer(serializers.ModelSerializer):
 


    class Meta:
       model = People
       fields = ('id', 'related_photo', 'related_user')










from rest_framework import serializers
from .models import User, Photo, People, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):



    class Meta:
       model = User
       fields = ('id', 'name', 'email', 'phone', 'password')






class PhotoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    


 


    class Meta:
       model = Photo
       fields = ('id', 'date', 'photo_name', 'preview_url', 'image','comment','user')




class PeopleSerializer(serializers.ModelSerializer):
 


    class Meta:
       model = People
       fields = ('id', 'related_photo', 'related_user')

class CommentSerializer(serializers.ModelSerializer):
 


    class Meta:
       model = Comment
       fields = ('id', 'rel_photo', 'rel_user', 'comment')











# tunr/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.parsers import MultiPartParser, FormParser



urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('photos/', views.PhotoList.as_view(), name='photo_list'),
    path('photos/<int:pk>', views.PhotoDetail.as_view(), name='photo_detail'),
    path('peoples/', views.PeopleList.as_view(), name='people_list'),
    path('peoples/<int:pk>', views.PeopleDetail.as_view(), name='people_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentList.as_view(), name='comment_detail'),
    path('comment/<int:pk>', views.CommentDetail.as_view(), name='comment_details'),
    path('photos/', views.PhotoList.as_view(), name='photo_list'),
    path('photos/<int:pk>/', views.PhotoDetail.as_view(), name='photo_detail'),
    path('photos/<int:photo_id>/comments/', views.CommentList.as_view(), name='comment_list'),
    path('photos/<int:photo_id>/comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
    path('photos/upload/', views.UploadPhoto.as_view(), name='upload_photo'),


]
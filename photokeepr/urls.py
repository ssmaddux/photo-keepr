# tunr/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('photos/', views.PhotoList.as_view(), name='photo_list'),
    path('photos/<int:pk>', views.PhotoDetail.as_view(), name='photo_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
    path('peoples/', views.PeopleList.as_view(), name='people_list'),
    path('peoples/<int:pk>', views.PeopleDetail.as_view(), name='people_detail'),

]
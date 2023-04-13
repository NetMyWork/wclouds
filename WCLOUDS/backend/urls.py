from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('blog/<str:pk>/', views.blog, name='blog'),
    path('gallery', views.gallery, name='gallery'),
    path('community/<str:pk>/', views.community, name='community'),
    path('mycommunities',views.mycommunity,name='mycommunity'),
    path('cloud/<str:pk>/', views.cloud, name='cloud'),
    path('like/<str:pk>/', views.likepost, name='like'),
    path('mail',views.mail,name='mail'),
    path('save/<str:pk>/', views.save, name='save'),
    path('share/<str:pk>/', views.share, name='share'),
    path('sent/',views.sent,name='sent'),
    path('getmails/',views.getMessages,name='getmessage'),
    path('like-cloud/<str:pk>/', views.likecloud, name='like-cloud'),
    path('share-cloud/<str:pk>/', views.shareclouds, name='share-cloud'),
    path('messages/<str:pk>/', views.mymessages, name='mymessages'),
    path('blog/<str:pk>/', views.blog, name='blog'),
    ]
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework import generics
from .serializers import PostsSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Posts
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        order=self.request.GET.get('order')
        user=self.request.GET.get('user')
        offset=int(self.request.GET.get('offset'))
        limit=int(self.request.GET.get('limit'))
        if(order=="earliest"):
            queryset = self.queryset.exclude(user=self.request.user).order_by('-date_added')
        else:
            queryset = self.queryset.exclude(user=self.request.user)
        if(user):
            queryset = queryset.filter(user=user)
        return queryset

class MyPostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    pagination_class = None
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
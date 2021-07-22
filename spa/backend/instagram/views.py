from django.shortcuts import render
from rest_framework.permissions import AllowAny

from .models import Post
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer


# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny] # FIXME: 인증 적용
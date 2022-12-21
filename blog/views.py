from rest_framework import generics
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .permissions import IsCommentOwner, IsPostOwner


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Post.objects.select_related('owner').filter(is_published=True)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsPostOwner]

    def get_object(self):
        return get_object_or_404(Post, id=self.kwargs.get('pk'))


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Comment.objects.select_related('post', 'author').filter(is_published=True)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsCommentOwner]

    def get_object(self):
        return get_object_or_404(Comment, id=self.kwargs.get('pk'))

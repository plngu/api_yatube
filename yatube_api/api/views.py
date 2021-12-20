from django.shortcuts import get_object_or_404
from posts.models import Comment
from posts.models import Group
from posts.models import Post
from rest_framework import viewsets

from .mixins import CreateUpdateDestroyMixin
from .serializers import CommentSerializer
from .serializers import GroupSerializer
from .serializers import PostSerializer


class PostViewSet(CreateUpdateDestroyMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(CreateUpdateDestroyMixin):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if get_object_or_404(Post, pk=post_id):
            new_queryset = Comment.objects.filter(post=post_id)
            return new_queryset

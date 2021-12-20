from posts.models import Comment, Group, Post
from rest_framework import viewsets
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)

from .permissions import AuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class CreateUpdateDestroyMixin(CreateModelMixin,
                               DestroyModelMixin,
                               UpdateModelMixin,
                               ListModelMixin,
                               RetrieveModelMixin,
                               viewsets.GenericViewSet):
    permission_classes = [AuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


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
        if Post.objects.filter(pk=post_id):
            new_queryset = Comment.objects.filter(post=post_id)
            return new_queryset
        return []

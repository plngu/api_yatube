from rest_framework import viewsets

from .permissions import AuthorOrReadOnly


class CreateUpdateDestroyMixin(viewsets.ModelViewSet):
    permission_classes = [AuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

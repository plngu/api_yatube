from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls))
]

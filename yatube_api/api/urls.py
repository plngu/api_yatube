from django.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet
from .views import GroupViewSet
from .views import PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls))
]

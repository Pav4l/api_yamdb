from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserCreateViewSet,
                    UserReceiveTokenViewSet, UserViewSet)

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/',
         UserCreateViewSet.as_view({'post': 'create'}),
         name='signup'),
    path('auth/token/',
         UserReceiveTokenViewSet.as_view({'post': 'create'}),
         name='token')
]

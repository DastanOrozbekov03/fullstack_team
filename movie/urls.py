from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmViewset, CategoryViewset, LikeViewset, CommentViewset, FavoriteView



router = DefaultRouter()
router.register('categories', CategoryViewset)
router.register('films', FilmViewset)
router.register('like', LikeViewset)
router.register('comment', CommentViewset)
router.register('favorite', FavoriteView)


urlpatterns = [
    path('', include(router.urls)),
]
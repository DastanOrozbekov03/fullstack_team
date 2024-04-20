from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmViewset, CategoryViewset, FavoritView

router = DefaultRouter()
router.register('categories', CategoryViewset)
router.register('films', FilmViewset)
router.register('favorit', FavoritView)
from .views import FilmViewset, CategoryViewset, LikeViewset, CommentViewset, RatingViewset

router = DefaultRouter()
router.register('categories', CategoryViewset)
router.register('films', FilmViewset)
router.register('like', LikeViewset)
router.register('comment', CommentViewset)
router.register('favorite', FavoritView)
router.register('rating', RatingViewset)


urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmView, CategoryView, FavoritView

router = DefaultRouter()
router.register('categories', CategoryView)
router.register('films', FilmView)
router.register('favorit', FavoritView)
from .views import FilmViewset, CategoryViewset, LikeViewset, CommentViewset

router = DefaultRouter()
router.register('categories', CategoryViewset)
router.register('films', FilmViewset)
router.register('like', LikeViewset)
router.register('comment', CommentViewset)


urlpatterns = [
    path('', include(router.urls)),
]
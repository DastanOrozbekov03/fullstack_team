from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmView, CategoryView, FavoritView

router = DefaultRouter()
router.register('categories', CategoryView)
router.register('films', FilmView)
router.register('favorit', FavoritView)

urlpatterns = [
    path('', include(router.urls)),
]
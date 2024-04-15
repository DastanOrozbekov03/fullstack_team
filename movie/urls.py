from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmView, CategoryView

router = DefaultRouter()
router.register('categories', CategoryView)
router.register('films', FilmView)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlacesView, HallViewset, SeansViewset

router = DefaultRouter()
router.register('hall', HallViewset)
router.register('place', PlacesView)
router.register('seans', SeansViewset)


urlpatterns = [
    path('', include(router.urls)),
]
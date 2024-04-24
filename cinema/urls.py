from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HallViewset, SeatList, SeansViewset, BookingViewset

router = DefaultRouter()
router.register('hall', HallViewset)
router.register('booking', BookingViewset)
router.register('seans', SeansViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('seats/', SeatList.as_view())
]
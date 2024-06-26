from rest_framework.viewsets import ModelViewSet 
from rest_framework import generics
from .serializers import HallSerializer, SeatSerializer, SeansSerializer, BookingSerializers
from .models import Hall, Seat, Seans, Booking
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class PermissionMixin:
    def get_permissions(self):
        if self.action in ('retrive', 'list'):
            permissions = [AllowAny]
        else:
            permissions = [IsAdminUser]
        return [permission() for  permission in permissions]        


class HallViewset(PermissionMixin, ModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer

class SeatList(generics.ListAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class SeansViewset(PermissionMixin, ModelViewSet):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializer

class BookingViewset(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
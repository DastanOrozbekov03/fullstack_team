from rest_framework.viewsets import ModelViewSet 
from rest_framework.generics import CreateAPIView
from .serializers import PlacesSerializers, HallSerializers, SeansSerializers
from .models import Places, Hall, Seans



class PlacesView(ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializers

class HallViewset(ModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = HallSerializers

class SeansViewset(ModelViewSet):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializers
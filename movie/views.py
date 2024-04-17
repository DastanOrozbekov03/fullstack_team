from rest_framework.viewsets import ModelViewSet
from .models import Film, Category, Favorite
from .serializers import Categoryserializers, FilmSerializers, FavoriteSerializer
from rest_framework.response import Response

class FilmView(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserializers

class FavoritView(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response('film delete', status = 200)
        except:
            return Response('film not found', status = 200)
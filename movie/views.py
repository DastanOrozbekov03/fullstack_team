from rest_framework.viewsets import ModelViewSet
from .models import Film, Category
from .serializers import Categoryserializers, FilmSerializers

class FilmView(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers()

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserializers()
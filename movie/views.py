from rest_framework.viewsets import ModelViewSet
from .models import Film, Category, Favorite
from .serializers import CategorySerializers, FilmSerializers, FavoriteSerializer, RatingSerializer, MovieShortSerilaizer, GenreSerializer
from rest_framework.response import Response
from .models import Film, Category, Comment, Like, Rating, MovieShorts, Genre
from .serializers import CategorySerializers, FilmSerializers, CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import action
from .permissions import BlockPermission, IsAuthorPermission
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class FilmViewset(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'slug', 'title'] 
    search_fields = ['title']

    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

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


class LikeViewset(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
    def get_serializer_context(self):
        return {'request':self.request}

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args,**kwargs)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in 'destroy':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [BlockPermission]
        return super().get_permissions()

class CommentViewset(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in 'destroy':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthorPermission]
        return super().get_permissions()
    
class GenreViewset(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class RatingViewset(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in 'destroy':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthorPermission]
        return super().get_permissions()    
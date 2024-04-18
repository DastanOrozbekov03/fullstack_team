from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Film, Category, Comment, Like, Favorite
from .serializers import CategorySerializers, FilmSerializers, CommentSerializer, LikeSerializer, FavoriteSerializer
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import action

from .permissions import BlockPermission




class FilmViewset(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'slug', 'title'] 
    search_fields = ['title']

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()




class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers



class FavoriteView(ModelViewSet):
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
 



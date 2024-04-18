from rest_framework.viewsets import ModelViewSet
from .models import Film, Category, Favorite
from .serializers import CategorySerializers, FilmSerializers, FavoriteSerializer
from rest_framework.response import Response
from .models import Film, Category, Comment, Like
from .serializers import CategorySerializers, FilmSerializers, CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import action
from .permissions import BlockPermission


class FilmViewset(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

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


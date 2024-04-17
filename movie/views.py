from rest_framework.viewsets import ModelViewSet
from .models import Film, Category, Comment, Like
from .serializers import CategorySerializers, FilmSerializers, CommentSerializer, LikeSerializer
from drf_yasg.utils import swagger_auto_schema
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
    
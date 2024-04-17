from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Film, Category, Like, Comment
from rest_framework import serializers

class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FilmSerializers(ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class FilmListSerializers(ModelSerializer):
    class Meta:
        model = Film
        fields = ('title', 'image', 'ganre', 'year')

class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    # replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['author'] = user 
        return super().create(validated_data)
    
    # def get_replies(self, obj):
    #     replies = Comment.objects.filter(parent_comment=obj)
    #     serializer = CommentSerializer(replies, many=True)
    #     return serializer.data    
    
class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['author'] = user 
        return super().create(validated_data)
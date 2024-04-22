from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Film, Category, Like, Comment, Favorite, Rating, MovieShorts, Genre
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FilmSerializers(ModelSerializer):
    class Meta:
        model = Film
        fields = ('title', 'image', 'ganre', 'year')

    def get_average_rating(self, obj):
        ratings = Rating.objects.filter(movie=obj)
        if ratings.exists():
            return sum([rating.star for rating in ratings]) / len(ratings)
        return 0    

class FavoriteSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Favorite
        fields = ('author', 'film')

    def create(self, validated_data):
        author = self.context['request'].user
        validated_data['author'] = author
        return super().create(validated_data)

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
    
    # def get_likes_count(self, instanse):
    #     return instanse.likes.count()
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['likes_count'] = self.get_likes_count(instance)
    #     return representation
    
    # def get_replies(self, obj):
    #     replies = Comment.objects.filter(parent_comment=obj)
    #     serializer = CommentSerializer(replies, many=True)
    #     return serializer.data

class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source = 'author.email')

    class Meta:
        model = Like
        fields = '__all__'


    def create(self, validated_data):
        request = self.context.get('request')
        # print(request.user)
        # print('!!!!!!!!!!!!!')
        author = request.user
        validated_data['author'] = author
        return super().create(validated_data)
 

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ('author', 'star', 'film')

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('title', 'slug')
    
class MovieShortSerilaizer(ModelSerializer):
    class Meta:
        model = MovieShorts
        fields = ('title')

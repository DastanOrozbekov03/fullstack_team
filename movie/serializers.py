from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Film, Category, Like, Comment, Favorite, Rating, MovieShorts, Genre
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['title']

    def to_representation(self, instance):
        representation = super().to_representation(instance) 
        representation['genre'] = instance.title
        return representation


class FilmSerializers(ModelSerializer):
    ganre = GenreSerializer(many=True) 

    class Meta:
        model = Film
        fields = ['title', 'image', 'ganre', 'year']
  
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

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['author'] = user
        return super().create(validated_data)        
    

class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source = 'author.email')

    class Meta:
        model = Like
        fields = '__all__'


    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        validated_data['author'] = author
        return super().create(validated_data)
 

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ('author', 'star', 'film')

class MovieShortSerilaizer(ModelSerializer):
    class Meta:
        model = MovieShorts
        fields = ('title')


from rest_framework import serializers
from .models import Film, Category, Favorite
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('title', 'image', 'ganre', 'year')

class FavoriteSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Favorite
        fields = ('author', 'film')

    def create(self, validated_data):
        author = self.context.get('request').user
        validated_data['author'] = author
        return super().create(validated_data)
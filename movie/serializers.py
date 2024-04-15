from rest_framework import serializers
from .models import Film, Category


class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
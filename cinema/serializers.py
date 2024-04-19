from rest_framework import serializers
from .models import Hall, Places, Seans


class HallSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ('name', 'places')   

class PlacesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__'    

class SeansSerializers(serializers.ModelSerializer):
    class Meta:
        model = Seans
        fields = '__all__'
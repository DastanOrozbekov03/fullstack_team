from rest_framework import serializers
from .models import Hall, Row, Seat, Seans, Booking

class SeansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seans
        fields = '__all__'

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'

class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
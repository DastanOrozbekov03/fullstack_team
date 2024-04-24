from django.db import models
from django.core.validators import MaxValueValidator
from movie.models import Film
from django.contrib.auth import get_user_model
    
User = get_user_model()


class Hall(models.Model):
    # film = models.ForeignKey(Film, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)  
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)


class Seans(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='hall_for_seans')
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, primary_key=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.film.title} at {self.hall.name} ({self.start_time})"

class Row(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='rows')
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"Row {self.name} in Hall {self.hall.name}"

    def get_seats(self):
        return self.seats.all()
    
class Seat(models.Model):
    row = models.ForeignKey(Row, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.PositiveIntegerField()
    booked = models.BooleanField(default=False)  # Флаг забронированного места

    def __str__(self):
        return f"Row {self.row.name}, Seat {self.seat_number} in Hall {self.row.hall.name}"


class Booking(models.Model):
    seans = models.ForeignKey('Seans', on_delete=models.CASCADE)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"booking {self.seans}"
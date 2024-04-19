from django.db import models
from django.core.validators import MaxValueValidator
from movie.models import Film
# from booking.models import Seans

    
class Hall(models.Model):
    # film = models.ForeignKey(Film, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)  
    places = models.PositiveIntegerField(validators=[MaxValueValidator(40)])


    def __str__(self):
        return f"{self.film.name}-{self.name}"

class Seans(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='hall_for_seans')
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.film.title} at {self.hall.name} ({self.start_time})"



class Places(models.Model):
    id = models.IntegerField(primary_key=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='places_for_booking')

    def __str__(self) -> str:
        return f"{self.id} in {self.hall}"
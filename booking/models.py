from django.db import models
from movie.models import Film
from cinema.models import Seans
from django.contrib.auth import get_user_model

User = get_user_model()


# class Seans(models.Model):
#     # hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
#     film = models.ForeignKey(Film, on_delete=models.CASCADE)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()

#     def __str__(self):
#         return f"{self.film.title} at {self.hall.name} ({self.start_time})"
    

class Booking(models.Model):
    showtime = models.ForeignKey(Seans, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_numbers = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.user_name} - {self.hall} - Seats {self.seat_numbers}"
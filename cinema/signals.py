from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Hall, Row, Seat


@receiver(post_save, sender=Hall)
def create_default_rows_and_seats(sender, instance, created, **kwargs):
    """Создание рядов и мест при создании нового зала."""
    if created:
        for row_number in range(1, 6):  # Создаем 5 рядов
            row = Row.objects.create(hall=instance, name=f'Row {row_number}')
            for seat_number in range(1, 9):  # Создаем 8 мест в каждом ряду
                Seat.objects.create(row=row, seat_number=seat_number)
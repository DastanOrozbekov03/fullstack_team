# Generated by Django 5.0.4 on 2024-04-23 14:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='cinema.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Seans',
            fields=[
                ('slug', models.SlugField(blank=True, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.film')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hall_for_seans', to='cinema.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.PositiveIntegerField()),
                ('booked', models.BooleanField(default=False)),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='cinema.row')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('seans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.seans')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.seat')),
            ],
        ),
    ]

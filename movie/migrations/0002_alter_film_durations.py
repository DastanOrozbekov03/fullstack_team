# Generated by Django 5.0.4 on 2024-04-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='durations',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
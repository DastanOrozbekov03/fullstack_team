from django.db import models
from slugify import slugify

class Category(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, primary_key=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

class Film(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, primary_key=True, blank=True)
    description = models.TextField(blank=True)
    tagline = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='films')
    country = models.CharField(max_length=100, unique=True)
    actors = models.CharField(max_length=500, blank=True)
    stage_director = models.CharField(max_length=100)
    year = models.PositiveIntegerField(default=2020)
    ganre = models.CharField(max_length=100)
    primera = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

        sdfghjkl
from django.db import models
from slugify import slugify
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, primary_key=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

class Genre(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title



class Film(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='films', null=True)
    slug = models.SlugField(max_length=200, primary_key=True, blank=True)
    description = models.TextField(blank=True)
    durations = models.PositiveIntegerField(blank=True)
    tagline = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/', blank=True)
    country = models.CharField(max_length=100)
    actors = models.CharField(max_length=500, blank=True)
    stage_director = models.CharField(max_length=100, blank=True)
    year = models.PositiveIntegerField(default=2020)
    ganre = models.ManyToManyField(Genre)
    primera = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

class MovieShorts(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movie_shorts/', blank=True)

    def __str__(self) -> str:
        return self.title
    
class Rating(models.Model):
    RATING_CHOICES = [
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='ratings_film')
    star = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
        
    # class Meta:
    #     unique_together = ('author', 'film')

    def __str__(self) -> str:
        return f"{self.author} {self.star} - {self.film}"


class Favorite(models.Model):
    author = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, related_name='favorites', on_delete=models.CASCADE)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
    # comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)

    def __str___(self):
        return self.body
    
class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='likes', null=True)
    # comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='likes', blank=True, null=True)

    def __str__(self) -> str:
        return f'liked by {self.author.email}'


from django.db import models
from slugify import slugify
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, primary_key=True, blank=True)

    def str(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

class Film(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='films')
    slug = models.SlugField(max_length=200, primary_key=True, blank=True)
    description = models.TextField(blank=True)
    tagline = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/', blank=True)
    country = models.CharField(max_length=100)
    actors = models.CharField(max_length=500, blank=True)
    stage_director = models.CharField(max_length=100)
    year = models.PositiveIntegerField(default=2020)
    ganre = models.CharField(max_length=100)
    primera = models.CharField(max_length=20)

    def str(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


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
    # parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)

    def str(self):
        return self.body
    
class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='likes', blank=True, null=True)
    # comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='likes', blank=True, null=True)

    def str(self) -> str:
        return f'liked by {self.author.email}'


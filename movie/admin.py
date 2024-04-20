from django.contrib import admin
from .models import Film, Like, Comment, Category, Favorite, Rating, Genre
from django.utils.safestring import mark_safe


class FilmAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['category', 'title']
    search_fields = ['title', 'ganre']
    

admin.site.register(Film, FilmAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Rating)
admin.site.register(Genre)


from django.contrib import admin
from .models import Film, Like, Comment, Category, Favorite, Genre


admin.site.register(Film)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Genre)
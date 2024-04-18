from django.contrib import admin
from .models import Film, Like, Comment, Category, Favorite


admin.site.register(Film)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Favorite)

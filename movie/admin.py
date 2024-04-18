from django.contrib import admin
from .models import Film, Like, Comment, Category, Favorite



class FilmAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['category', 'title']
    search_fields = ['title', 'ganre']
    # inlines = []


admin.site.register(Film, FilmAdmin)
admin.site.register(Film)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Favorite)

from django.contrib import admin
from .models import Film




class FilmAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['category', 'title']
    search_fields = ['title', 'ganre']
    # inlines = []


admin.site.register(Film, FilmAdmin)

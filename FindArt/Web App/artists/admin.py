from .models import Artist
from django.contrib import admin

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    list_display_links = ('full_name',)
    search_fields = ('full_name',)
    list_per_page = 15

# Register your models here.
admin.site.register(Artist, ArtistAdmin)
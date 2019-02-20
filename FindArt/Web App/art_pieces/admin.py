from django.contrib import admin

from .models import Art_Pieces

class Art_PiecesAdmin(admin.ModelAdmin):
  list_display = ('title', 'art_type', 'photo', 'date_entered', 'artist')
  list_display_links = ('title',)
  list_filter = ('artist',)
  search_fields = ('title', 'art_type', 'photo')
  list_per_page = 25

admin.site.register(Art_Pieces, Art_PiecesAdmin)

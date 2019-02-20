from django.urls import path 

from . import views

urlpatterns = [
    path('', views.art_pieces, name='art_pieces'),
    path('<int:artist_id>', views.art_piece, name='art_piece'),
    path('search', views.search, name='search'),
]
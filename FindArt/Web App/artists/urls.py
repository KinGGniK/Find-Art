from django.urls import path 

from . import views

urlpatterns = [
    path('artists', views.artists, name='artists'),
    path('<int:artist_id>', views.artist, name='artist'),
    path('search', views.search, name='search'),
]
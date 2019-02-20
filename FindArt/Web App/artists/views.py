from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Artist
from art_pieces.models import Art_Pieces

# Create your views here.
def artists(request):
    artists = Artist.objects.order_by('-date_entered')

    paginator = Paginator(artists, 10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'artists': artists
    }

    return render(request, 'artists/artists.html', context)

def artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    artist_list = Art_Pieces.objects.order_by('-date_entered').filter(artist_id=artist_id)

    context = {
        'artist': artist,
        'pieces' : artist_list
    }

    return render(request, 'artists/artist.html', context)

def search(request):
    return render(request, 'artists/search.html', context)
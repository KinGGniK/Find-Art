from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from listings.choices import art_choices
from .models import Art_Pieces
from artists.models import Artist

# Create your views here.
def art_pieces(request):
    pieces = Art_Pieces.objects.order_by('-date_entered')

    paginator = Paginator(pieces, 10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'pieces': pieces
    }

    return render(request, 'art_pieces/art_pieces.html', context)

def art_piece(request, artist_id):
    piece = get_object_or_404(Art_Pieces, pk=artist_id)

    context = {
        'piece': piece
    }
    return render(request, 'art_pieces/art_piece.html', context)

def search(request):
    queryset_list = Art_Pieces.objects.order_by('-date_entered')
    artists = Artist.objects.all()

    #Keywords/Title
    if 'title' in request.GET:
        keywords = request.GET['title']
        if keywords: 
            queryset_list = queryset_list.filter(title__icontains=keywords)

    #Artist
    if 'artist' in request.GET:
        artist = request.GET['artist']
        if artist: 
            queryset_list = queryset_list.filter(artist__full_name__icontains=artist)

    #Style
    if 'style' in request.GET:
        style = request.GET['style']
        if style: 
            queryset_list = queryset_list.filter(art_type__iexact=style)

    context = {
        'artists' : artists,
        'styles' : art_choices,
        'pieces' : queryset_list,
        'values' : request.GET
    }
    return render(request, 'art_pieces/search.html', context)
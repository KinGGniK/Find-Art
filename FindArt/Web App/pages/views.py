from django.shortcuts import render
from django.http import HttpResponse

from listings.choices import art_choices

from art_pieces.models import Art_Pieces
from artists.models import Artist
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    pieces = Art_Pieces.objects.order_by('-date_entered')[:3]
    artists = Artist.objects.all()

    context = {
        'pieces' : pieces,
        'artists' : artists,
        'styles' : art_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('hire_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
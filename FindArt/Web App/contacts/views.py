from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        piece_id = request.POST['piece_id']
        piece = request.POST['piece']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        artist_email = request.POST['artist_email']

        #Check if user has made inquiry
        if request.user.is_authenticated:
                user_id = request.user.id
                has_contacted = Contact.objects.all().filter(piece_id=piece_id, user_id=user_id)
                if has_contacted:
                        messages.error(request, 'An inquiry has already been made')
                        return redirect('/art_pieces/' + piece_id)

        contact = Contact(piece=piece, piece_id=piece_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        #Sends Email
        send_mail(
                'Art Piece Inquiry',
                'There has been an inquiry ' + piece + '. Sign into the admin panel for more info',
                'ivensky360@gmail.com',
                [artist_email, 'ivenskywat@gmail.com'],
                fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, the artist should get back to you soon')

        return redirect('/art_pieces/' + piece_id)
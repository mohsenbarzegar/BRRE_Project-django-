from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

    # Check if that user already made inquery
    if request.user.is_authenticated:
        user_id = request.user.id
        has_contracted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        if has_contracted:
            messages.error(request, "You have already inquery for this listing")
            return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
    user_id=user_id)

    contact.save()
    # Send mail
    # send_mail(
    #     'Property Listing inquery',
    #     'There has been inquery for' + listing + '. Sign into the admin panel for more info.',
    #     'mohsenbarzegar94@gmail.com',
    #     ['mohsenbarzegar94@gmail.com'],
    #     fail_silently=False,
    # )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+listing_id)
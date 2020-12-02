import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact


def contact(request):
    if request.method == "POST":
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        email = request.POST['email']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if logged in User has made an enqury before
        if request.user.is_authenticated:
            """Set user id to request id and Check Contact Model for any related listing"""
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                user_id=user_id, listing_id=listing_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inqury for this listing')
                return redirect('/listings/' + listing_id)

        # Save enqury into database
        contact = Contact(
            listing=listing,
            name=name,
            email=email,
            message=message,
            phone=phone,
            user_id=user_id,
            listing_id=listing_id)

        contact.save()

        # Send email
        send_mail(
            'Property Listing enqury',
            'There has been an inqury for ' + listing +
            '. Sign into admin panel for more information.',
            'quilltech57@gmail.com',
            [realtor_email, 'ugbemjob57@gmail.com'],
            fail_silently=False,
        )
        messages.success(
            request, 'Your request has been submitted, we\'ll get back to you as soon as possible')

    return redirect('/listings/' + listing_id)

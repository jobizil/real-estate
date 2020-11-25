from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing


def index(request):
    """ Gets item listings in db """
    listings = (
    Listing.objects
        ).order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)      # Set Pagination
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = { 'listings':paged_listings }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """ Gets items listing by its id """
    return render(request, 'listings/listing.html')


def search(request):
    """ Provides functionality to perform search """
    return render(request, 'listings/search.html')

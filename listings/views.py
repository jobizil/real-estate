from django.shortcuts import render

# Gets item listings in db
def listings(request):
    return render(request, 'listings/listings.html')

# Gets items listing by its id
def listing(request):
    return render(request, 'listings/listing.html')

# Provides functionality to perform search
def search(request):
    return render(request, 'listings/search.html')

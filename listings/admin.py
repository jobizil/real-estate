from django.contrib import admin
from .models import  Listing


class ListingAdmin(admin.ModelAdmin):
    """Displays a table of items in the admin page """
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')    # Set clickable items
    list_filter = ('realtor',)      #Set filter items
    list_editable = ('is_published',)       #Set Checkbox on bool
    search_fields = ('title', 'address', 'city', 'price', 'zipcode', 'description')     #Set Search Option
    list_per_page = 20    #pagination 

admin.site.register(Listing, ListingAdmin)
